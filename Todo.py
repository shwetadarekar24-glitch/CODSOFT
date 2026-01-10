This Python program is a simple command-line To-Do List application that allows users to add, view, and delete tasks, helping them organize and manage their daily activities efficiently.

  tasks = []

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    ch = input("Enter choice: ")

    if ch == '1':
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added")

    elif ch == '2':
        if not tasks:
            print("No tasks")
        else:
            for i, t in enumerate(tasks, 1):
                print(i, t)

    elif ch == '3':
        n = int(input("Enter task number to delete: "))
        if 1 <= n <= len(tasks):
            tasks.pop(n-1)
            print("Task deleted")
        else:
            print("Invalid task number")

    elif ch == '4':
        print("Goodbye!")
        break

    else:
        print("Invalid choice")
