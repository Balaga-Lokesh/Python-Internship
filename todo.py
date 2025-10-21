TODO_FILE = "tasks.txt"

def load_tasks():
    try:
        with open(TODO_FILE, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def view_tasks(tasks):
    print("\n=== Your To-Do List ===")
    if not tasks:
        print("No tasks found!")
    else:
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

def add_task(tasks):
    task = input("Enter new task: ").strip()
    if task:
        tasks.append(task)
        print("Task added!")
    else:
        print("Empty task not added.")

def remove_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter task number to remove: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            print(f"Removed: {removed}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def clear_tasks(tasks):
    tasks.clear()
    print("All tasks cleared!")

def main():
    tasks = load_tasks()
    while True:
        print("\n=== To-Do List Menu ===")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Clear All Tasks")
        print("5. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            clear_tasks(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("All changes saved. Goodbye!")
            break
        else:
            print("Invalid choice, please try again!")

if __name__ == "__main__":
    main()
