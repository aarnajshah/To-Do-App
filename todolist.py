import time


todo_list = []


def add_task(task, priority):  # Added 'priority' as a parameter
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    # Changed to store tasks as dictionaries for better attribute handling
    todo_list.append({"task": task, "priority": priority, "due_date": None, "timestamp": timestamp})
    print(f"Task '{task}' added successfully with priority '{priority}' on {timestamp}.")


def view_tasks():
    if todo_list:
        print("\nYour To-Do List:")
        # Updated to reflect the new dictionary structure
        for i, task in enumerate(todo_list, 1):
            print(
                f"{i}. {task['task']} (Priority: {task['priority']}, Added on: {task['timestamp']}, Due Date: {task['due_date'] or 'None'})"
            )
    else:
        print("\nYour To-Do List is empty.")


def remove_task(task_number):
    if 0 < task_number <= len(todo_list):
        # Updated to handle dictionary-based tasks
        removed_task = todo_list.pop(task_number - 1)
        print(f"Task '{removed_task['task']}' removed successfully (added on {removed_task['timestamp']}).")
    else:
        print("Invalid task number.")


def edit_task(task_number):
    if 0 < task_number <= len(todo_list):
        task = todo_list[task_number - 1]  # Access the specific task using its index
        print(
            f"Editing task '{task['task']}' (current priority: {task['priority']}, current due date: {task['due_date'] or 'None'})."
        )

        # Allow user to modify task description
        new_task = input("Enter new task description (leave empty to keep current): ") or task['task']
        # Allow user to modify task priority
        new_priority = input("Enter new priority (leave empty to keep current): ") or task['priority']
        # Allow user to modify due date
        new_due_date = input("Enter a new due date (leave empty to keep current): ") or task['due_date']

        # Update the task
        task['task'] = new_task
        task['priority'] = new_priority
        task['due_date'] = new_due_date

        print("Task updated successfully.")
    else:
        print("Invalid task number.")


def main():
    while True:
        print("\nOptions: (1) Add Task (2) View Tasks (3) Edit Task (4) Remove Task (5) Exit")
        choice = input("Enter the number of your choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            priority = input("Is this task... a. very important  b. important  c. not important? Enter the letter of your choice: ").lower()
            priority_map = {"a": "Very Important", "b": "Important", "c": "Not Important"}
            priority = priority_map.get(priority, "Not Specified")  # Map user input to readable priorities
            add_task(task, priority)  # Pass priority to add_task
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            view_tasks()
            try:
                task_number = int(input("Enter the task number to edit: "))
                edit_task(task_number)  # Call edit_task with the correct task number
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            view_tasks()
            try:
                task_number = int(input("Enter the task number to remove: "))
                remove_task(task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '5':
            print("Goodbye!\n")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()