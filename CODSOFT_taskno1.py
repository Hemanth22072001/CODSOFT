''' Creating a empty List to store items/tasks '''
tasks=[]

'''To add a item/task'''
def add_task():
    task=input("Enter a new task to be inserted: ")
    tasks.append(task)
    print("Task Inserted Successfully.")

'''To view all tasks'''
def all_tasks():
    if len(tasks)==0:
        print("There is no tasks to display.")
    else:
        print("\n----List of Tasks----")
        for i, task in enumerate(tasks):
            print(f'{i+1}. {task}')
        print("---End List---")

'''To delete the tasks'''
def del_task():
    if len(tasks)==0:
        print("There is no tasks to delete.")
    else:
        print("----Tasks----")
        for i, task in enumerate(tasks):
            print(f'{i+1}. {task}')
        choice=int(input("Enter the task number to be deleted: "))

        if 0 < choice <= len(tasks):
            del tasks[choice-1]
            print("Task deleted successfully.")
        else:
            print("Invalid task number.")
    
'''main'''
def main():
    while True:
        print("\n----TO-DO-LIST MENU----")
        print("1. ADD TASKS")
        print("2. DELETE TASKS")
        print("3. SHOW LIST OF TASKS")
        print("4. EXIT")

        n=int(input("Enter your choice from above listed menu: "))
        if n == 1:
            add_task()
        elif n == 2:
            del_task()
        elif n == 3:
            all_tasks()
        elif n == 4:
            print("Thank You For Using TO-DO-LIST Application.")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
    