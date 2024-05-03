def show_menu():
    tasks = []
    menu_options = {
        1:"Add a task",
        2:"Remove a task",
        3:"View tasks",
        4:"Save tasks to a file",
        5:"Load tasks from a file",
        6:"Exit the application"
    }
#Menu work
    while True:
        print("\nTask Management Menu: ")
        for key in menu_options:
            print(f"{key}. {menu_options[key]}")

        try:
            choice = int(input("Please choose options (1-6)  "))
            if choice in menu_options:
                if choice == 6:
                    print("You are exiting ")
                    break
                else:
                    choice_handle(choice, tasks)
            else:
                print("Invaled option, Enter numbers between 1 and 6 ")
        except ValueError:
            print("Invalid input, Please enter a numerical input. ")
def choice_handle(choice, tasks):
    if choice == 1:
        task = input("Enter task to do ")  
        tasks.append(task) 
        print("Task added ")

    elif choice == 2:
        task = input("Enter the task to remove: ")
        try:
            tasks.remove(task)
            print("Task removed. ")
        except ValueError:
            print("Task not found")
    elif choice == 3:
        print("Tasks: ")
        for task in tasks:
            print(task)
            
    elif choice == 4:
        with open("tasks.txt",'w') as file:
            for task in tasks:
                file.write(task + '\n')
        print("Tasks saved to a file")   

    elif choice == 5:
        try:
            with open('tasks.txt', 'r') as file:
                tasks.extend(file.read().splitlines())
            print("Tasks loaded from file. ")
        except FileNotFoundError:
            print("No saved tasks file found")

       


if __name__ == "__main__":
    show_menu()