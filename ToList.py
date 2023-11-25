class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added successfully.")

    def delete_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Task '{task}' deleted successfully.")
        else:
            print(f"Task '{task}' not found.")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            print("Tasks:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")

def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Display Tasks")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            task = input("Enter task: ")
            todo_list.add_task(task)

        elif choice == '2':
            if todo_list.tasks:
                print("Current Tasks:")
                todo_list.display_tasks()
                task_index = int(input("Enter the number of the task to delete: "))
                if 1 <= task_index <= len(todo_list.tasks):
                    task_to_delete = todo_list.tasks[task_index - 1]
                    todo_list.delete_task(task_to_delete)
                else:
                    print("Invalid task number.")
            else:
                print("No tasks to delete.")

        elif choice == '3':
            todo_list.display_tasks()

        elif choice == '4':
            print("Exiting To-Do List Application. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
