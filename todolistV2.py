import time
# import turtle

todo_list = []
# pen = turtle.Turtle()
# pen.hideturtle()
# screen = turtle.Screen()
# screen.bgcolor('#d0f7ee')

def add_task(task, priority, due_date):  # Added 'priority' and 'due_date' as parameters
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    # Changed to store tasks as dictionaries for better attribute handling
    todo_list.append({"task": task, "priority": priority, "due_date": due_date, "timestamp": timestamp})
    print(f"\nTask '{task}' added successfully with priority '{priority}' and due date '{due_date}' on {timestamp}.")


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
        print(f"\nTask '{removed_task['task']}' removed successfully (added on {removed_task['timestamp']}).")
    else:
        print("\nInvalid task number.")


def edit_task(task_number):
    if 0 < task_number <= len(todo_list):
        task = todo_list[task_number - 1]  # Access the specific task using its index
        print(
            f"\nEditing task '{task['task']}' (current priority: {task['priority']}, current due date: {task['due_date'] or 'None'})."
        )

        # Allow user to modify task description
        new_task = input("Enter new task description (leave empty to keep current): ") or task['task']
        # Allow user to modify task priority
        new_priority = input("Type out a new priority (leave empty to keep current): ") or task['priority']
        # Allow user to modify due date
        new_due_date = input("Enter a new due date (leave empty to keep current): ") or task['due_date']

        # Update the task
        task['task'] = new_task
        task['priority'] = new_priority
        task['due_date'] = new_due_date

        print("\nTask updated successfully.")
    else:
        print("\nInvalid task number.")


def main():
    while True:
        # pen.write("Options:   (1) Add Task   (2) Remove Task   (3) Edit Task   (4) View Tasks   (5) Exit", align="center", font="Arial")
        print("\nOptions: (1) Add Task (2) Remove Task (3) Edit Task (4) View Tasks (5) Exit")
        choice = input("\nEnter the number of your choice: ")

        if choice == '1':
            task = input("\nEnter the task: ")
            priority = input("\nIs this task... A. very important  B. important  C. not important?   Enter the letter of your choice: ").lower()
            print()
            priority_map = {"a": "Very Important", "b": "Important", "c": "Not Important"}
            priority = priority_map.get(priority, "Not Specified")  # Map user input to readable priorities
            due_date = input("\nEnter the due date of this task (mm/dd/yyyy): ")
            add_task(task, priority, due_date)  # Pass priority to add_task
        elif choice == '2':
            view_tasks()
            try:
                task_number = int(input("\nEnter the task number to remove: "))
                remove_task(task_number)
            except ValueError:
                print("\nPlease enter a valid number.")
        elif choice == '3':
            view_tasks()
            try:
                task_number = int(input("\nEnter the task number to edit: "))
                edit_task(task_number)  # Call edit_task with the correct task number
            except ValueError:
                print("\nPlease enter a valid number.")
        elif choice == '4':
            view_tasks()
        elif choice == '5':
            print("\nGoodbye!\n")
            break
        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()