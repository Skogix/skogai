import pygame

class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 10, 100)

    def move(self, dy):
        self.rect.y += dy
        self.rect.y = max(0, min(600 - self.rect.height, self.rect.y))  # Keep paddle on the screen

class Ball:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 15, 15)
        self.speed_x = 5
        self.speed_y = 5

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        # Collision with top and bottom
        if self.rect.top <= 0 or self.rect.bottom >= 600:
            self.speed_y *= -1

def handle_input(paddle1, paddle2):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddle1.move(-10)
    if keys[pygame.K_s]:
        paddle1.move(10)
    if keys[pygame.K_UP]:
        paddle2.move(-10)
    if keys[pygame.K_DOWN]:
        paddle2.move(10)

def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Pong Game')
    
    paddle1 = Paddle(50, 300)
    paddle2 = Paddle(740, 300)
    ball = Ball(400, 300)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        handle_input(paddle1, paddle2)
        ball.move()

        # Collision detection
        if ball.rect.colliderect(paddle1.rect) or ball.rect.colliderect(paddle2.rect):
            ball.speed_x *= -1

        # Clear the screen
        screen.fill((0, 0, 0))
        # Draw paddles and ball
        pygame.draw.rect(screen, (255, 255, 255), paddle1.rect)
        pygame.draw.rect(screen, (255, 255, 255), paddle2.rect)
        pygame.draw.ellipse(screen, (255, 255, 255), ball.rect)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
