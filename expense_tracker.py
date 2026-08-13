# Student Expense Tracker

print("💰 Student Expense Tracker")
print("--------------------------")

expenses = []

while True:
    print("\nChoose an option:")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Calculate total")
    print("4. Exit")

    choice = input("\nEnter your choice (1-4): ")

    if choice == "1":
        name = input("What did you spend money on? ")
        amount = input("How much did it cost? ")

        try:
            amount = float(amount)

            if amount < 0:
                print("❌ Amount cannot be negative.")
                continue

            expense = {
                "name": name,
                "amount": amount
            }

            expenses.append(expense)
            print("✅ Expense added successfully!")

        except ValueError:
            print("❌ Please enter a valid number.")

    elif choice == "2":
        if not expenses:
            print("\n📭 No expenses recorded yet.")
        else:
            print("\n📋 Your Expenses:")
            print("-----------------")

            for expense in expenses:
                print(f"{expense['name']}: ₹{expense['amount']:.2f}")

    elif choice == "3":
        total = sum(expense["amount"] for expense in expenses)

        print(f"\n💰 Total spending: ₹{total:.2f}")

    elif choice == "4":
        print("👋 Thanks for using Student Expense Tracker!")
        break

    else:
        print("❌ Invalid choice. Please select 1-4.")


