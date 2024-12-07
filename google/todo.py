import datetime

todos = []

def add_todo():
    """Adds a new todo item to the list."""
    task = input("Enter your todo item: ")
    due_date_str = input("Enter due date (YYYY-MM-DD, optional): ")
    due_date = datetime.datetime.strptime(due_date_str, "%Y-%m-%d").date() if due_date_str else None
    priority = input("Enter priority (high, medium, low, optional): ").lower() or "medium"
    todo = {"task": task, "due_date": due_date, "priority": priority, "completed": False}
    todos.append(todo)
    print("Todo added!")

def view_todos():
    """Displays all todo items."""
    if not todos:
        print("No todos yet!")
        return

    for i, todo in enumerate(todos):
        status = "[X]" if todo["completed"] else "[ ]"
        print(f"{i+1}. {status} {todo['task']} - Due: {todo['due_date'] or 'N/A'}, Priority: {todo['priority']}")

def mark_complete():
    """Marks a todo item as complete."""
    view_todos()
    try:
        index = int(input("Enter the number of the todo to mark as complete: ")) - 1
        if 0 <= index < len(todos):
            todos[index]["completed"] = True
            print("Todo marked as complete!")
        else:
            print("Invalid todo number.")
    except ValueError:
        print("Invalid input.")


def delete_todo():
    """Deletes a todo item."""
    view_todos()
    try:
        index = int(input("Enter the number of the todo to delete: ")) - 1
        if 0 <= index < len(todos):
            del todos[index]
            print("Todo deleted!")
        else:
            print("Invalid todo number.")
    except ValueError:
        print("Invalid input.")


while True:
    print("\nTodo Manager")
    print("1. Add todo")
    print("2. View todos")
    print("3. Mark as complete")
    print("4. Delete todo")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_todo()
    elif choice == "2":
        view_todos()
    elif choice == "3":
        mark_complete()
    elif choice == "4":
        delete_todo()
    elif choice == "5":
        break
    else:
        print("Invalid choice.")

print("Exiting...")
# ```
#
# To use this:
#
# 1.  Save the code as a Python file (e.g., `todo_manager.py`).
# 2.  Run it from your terminal: `python todo_manager.py`
#
# Remember that this is a very basic example.  To make it more useful, consider these improvements:
#
# *   **Persistence:** Save and load the todo list from a file (e.g., using JSON or a database like SQLite).
# *   **Error Handling:** Add more robust error handling (e.g., for invalid date formats).
# *   **UI:** Create a graphical user interface (GUI) using libraries like Tkinter, PyQt, or a web framework.
# *   **Filtering/Sorting:** Allow users to filter and sort todos by due date, priority, etc.
# *   **Search:** Add a search functionality to find specific todos.
#
#
# This improved version provides a foundation you can build upon to create a more sophisticated todo-manager.  Let me know if you'd like help with any of these improvements!
