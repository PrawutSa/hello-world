class Task:
    def __init__(self, title):
        self.title = title
        self.completed = False

    def complete(self):
        self.completed = True

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.title}"

tasks = []

while True:
    print("\nTo-do App")
    print("1. Add task")
    print("2. Complete task")
    print("3. Show tasks")
    print("4. Quit")

    choice = input("Enter choice (1-4): ")

    if choice == '1':
        title = input("Enter task title: ")
        tasks.append(Task(title))
        print(f"Task '{title}' added!")
    elif choice == '2':
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")
        task_num = int(input("Enter task number to complete: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num-1].complete()
            print("Task completed!")
        else:
            print("Invalid task number")
    elif choice == '3':
        print("\nYour tasks:")
        for task in tasks:
            print(task)
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice")