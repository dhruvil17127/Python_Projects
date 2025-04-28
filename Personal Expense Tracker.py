expenses = []  

while True:
    print("\n--- Expense Tracker ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        item = input("What did you spend on?: ")
        amount = float(input("How much? ₹"))
        expenses.append((item, amount))
        print("Expense added!")
    
    elif choice == '2':
        if not expenses:
            print("No expenses recorded yet.")
        else:
            print("\nYour Expenses:")
            total = 0
            for idx, (item, amount) in enumerate(expenses, start=1):
                print(f"{idx}. {item}: ₹{amount}")
                total += amount
            print(f"Total: ₹{total}")
    
    elif choice == '3':
        if not expenses:
            print("No expenses to delete.")
        else:
            print("\nSelect expense to delete:")
            for idx, (item, amount) in enumerate(expenses, start=1):
                print(f"{idx}. {item}: ₹{amount}")
            try:
                del_index = int(input("Enter the number to delete: ")) - 1
                if 0 <= del_index < len(expenses):
                    removed = expenses.pop(del_index)
                    print(f"Deleted {removed[0]}: ₹{removed[1]}")
                else:
                    print("Invalid number.")
            except ValueError:
                print("Please enter a valid number.")
    
    elif choice == '4':
        print("Goodbye!")
        break
    
    else:
        print("Invalid choice. Try again.")
