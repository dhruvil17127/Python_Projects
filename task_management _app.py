def task():
    tasks = [] #emty list
    print("\n----WELCOME TO THE TASK MANAGEMENT APP----\n")

    total_task = int(input("Enter how many task you want to add = "))
    for i in range(1,total_task+1):
        task_name = input(f"Enter task {i} = ")
        tasks.append(task_name)

    print(f"Today's tasks are {tasks}\n")
    while True:
        
        print("1. Add Task")
        print("2. Update Tasks")
        print("3. Delete Task")
        print("4. View Task")
        print("5. Exit")
        
        operation = int(input("Choose an option: "))

        if operation == 1:
            add = input("Enter the task want to add = ")
            tasks.append(add)
            print(f"Task {add} has been successfully added...")
        
        elif operation == 2:
            updated_val = input("Enter tha task name you want to update = ")
            if updated_val in tasks:
                up = input("Enter new task = ")
                ind = tasks.index(updated_val)
                tasks[ind] = up
                print(f"Update task {updated_val}")

        elif operation == 3:
            del_val = input("Which task you want to delete = ")
            if del_val in tasks:
                ind =  tasks.index(del_val)
                del tasks[ind]
                print(f"Task {del_val} has been deleted...")
        
        elif operation == 4:
            print(f"Total tasks = {tasks}")     

        elif operation == 5:
            print("Closing the program...")
            break

        else:
           print("Invalid input") 

task()
