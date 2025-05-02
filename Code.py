import pickle

# Function to load tasks from the file
def load_tasks():
    try:
        with open('tasks.pkl', 'rb') as file:
            tasks = pickle.load(file)
    except (FileNotFoundError, EOFError):
        tasks = []
    return tasks

# Function to save tasks to the file
def save_tasks(tasks):
    with open('tasks.pkl', 'wb') as file:
        pickle.dump(tasks, file)

# Function to display the to-do list
def display_tasks(tasks):
    if not tasks:
        print("Your to-do list is empty.")
    else:
        for idx, task in enumerate(tasks, 1):
            status = 'Done' if task['completed'] else 'Not Done'
            print(f"{idx}. {task['task']} - {status}")

# Function to add a task
def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append({'task': task, 'completed': False})
    save_tasks(tasks)
    print(f"Task '{task}' added.")

# Function to mark a task as completed
def mark_completed(tasks):
    display_tasks(tasks)
    try:
        task_num = int(input("Enter task number to mark as completed: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]['completed'] = True
            save_tasks(tasks)
            print(f"Task {task_num} marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Function to delete a task
def delete_task(tasks):
    display_tasks(tasks)
    try:
        task_num = int(input("Enter task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"Task '{removed_task['task']}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main function to run the application
def main():
    tasks = load_tasks()

    while True:
        print("\n--- To-Do List ---")
        print("1. View tasks")
        print("2. Add a task")
        print("3. Mark a task as completed")
        print("4. Delete a task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_completed(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Exiting the To-Do List application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
