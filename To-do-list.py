def display_menu():
    print("Command-line to do application")
    print("1. View/Track To-do list")
    print("2. Add Task")
    print("3.Mark Task as Completed")
    print("4.Delete Task")
    print("5.Exit")

def view_todo_list(todo_list):
    if todo_list:
        print("Your To-do list:")
    for task in todo_list:
        print(task)
    
    else:
        print("Your To-do list is Empty!")


def add_task (todo_list,task):
    todo_list.append(task)
    print("Task added Successfully")
    

def mark_task_completed(todo_list,task_index):
    if 0<=task_index < len(todo_list):
        todo_list[task_index]+="(Completed)"
        print("Task Mark as Completed")
    else:
        print("Invalid Task index!")

def  delete_task(todo_list,task_index):
    if 0<=task_index <len(todo_list):
        del todo_list[task_index]
        print("Deleted Task Successfully")
    else:
        print("Invalid task Index!")


def main():
    todo_list = []

    while True:
        display_menu()
        choice=input("Enter Your Choice:  ")

        if choice == "1":
            view_todo_list(todo_list)
        elif choice =="2":
            task = input("Enter a Task to Add:")
            add_task(todo_list,task)
        elif choice =="3":
            task_index=int(input("Enter a Index of Task to be Completed"))
            mark_task_completed(todo_list,task_index)
        elif choice =="4":
            task_index=int(input("Enter a Index of a task to be deleted"))
            delete_task(todo_list,task_index)
        elif choice =="5":
            print("Exiting...")
            break
        else:
            print("Invalid Choice ,Please Try again.")

            if __name__ == "__main__":
                main()




    



