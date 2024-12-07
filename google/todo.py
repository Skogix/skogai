import datetime
import argparse

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

def mark_complete(index=None):
    """Marks a todo item as complete."""
    if index is None:
        view_todos()
        try:
            index = int(input("Enter the number of the todo to mark as complete: ")) - 1
        except ValueError:
            print("Invalid input.")
            return
        if 0 <= index < len(todos):
            todos[index]["completed"] = True
            print("Todo marked as complete!")
        else:
            print("Invalid todo number.")


def delete_todo(index=None):
    """Deletes a todo item."""
    if index is None:
        view_todos()
        try:
            index = int(input("Enter the number of the todo to delete: ")) - 1
        except ValueError:
            print("Invalid input.")
            return
        if 0 <= index < len(todos):
            del todos[index]
            print("Todo deleted!")
        else:
            print("Invalid todo number.")


def main():
    parser = argparse.ArgumentParser(description="Todo Manager")
    parser.add_argument("--add", action="store_true", help="Add a new todo")
    parser.add_argument("--view", action="store_true", help="View all todos")
    parser.add_argument("--complete", type=int, help="Mark a todo as complete by its number")
    parser.add_argument("--delete", type=int, help="Delete a todo by its number")

    args = parser.parse_args()

    if args.add:
        add_todo()
    elif args.view:
        view_todos()
    elif args.complete is not None:
        mark_complete(args.complete)
    elif args.delete is not None:
        delete_todo(args.delete)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
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
