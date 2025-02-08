#i = 5
 #while i < 35 :
  #  print(i)
    # i += 5# Simple To-Do App

def display_menu():
    print("\nTo-Do List App")
    print("------------------")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

def view_tasks(tasks):
    if not tasks:
        print("\nYour to-do list is empty!")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            status = "✅" if task["completed"] else "❌"
            print(f"{i}. {task['title']} - {status}")

def add_task(tasks):
    title = input("\nEnter the task: ")
    tasks.append({"title": title, "completed": False})
    print(f"Task '{title}' added!")

def mark_task_completed(tasks):
    if not tasks:
        print("\nNo tasks to complete!")
        return
    view_tasks(tasks)
    try:
        task_num = int(input("\nEnter the task number to mark as completed: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["completed"] = True
            print(f"Task '{tasks[task_num - 1]['title']}' marked as completed!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def delete_task(tasks):
    if not tasks:
        print("\nNo tasks to delete!")
        return
    view_tasks(tasks)
    try:
        task_num = int(input("\nEnter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Task '{removed_task['title']}' deleted!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("\nChoose an option (1-5): ")
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_task_completed(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("\nGoodbye!")
            break
        else:
            print("Invalid choice. Please try again!")

if __name__ == "__main__":
    main()



    

