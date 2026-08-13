# Student Expense Tracker

print("💰 Student Expense Tracker")
print("--------------------------")

expenses = []

# Load previously saved expenses
try:
    with open("expenses.txt", "r") as file:
        for line in file:
            parts = line.strip().split("|")

            if len(parts) == 3:
                name = parts[0]
                amount = float(parts[1])
                category = parts[2]

                expenses.append({
                    "name": name,
                    "amount": amount,
                    "category": category
                })

except FileNotFoundError:
    pass

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

        print("\nCategories:")
        print("1. 🍔 Food")
        print("2. 🚗 Transport")
        print("3. 📚 Education")
        print("4. 🎮 Entertainment")
        print("5. 🛍️ Shopping")
        print("6. 📦 Other")

        category_choice = input("Choose a category (1-6): ")

        categories = {
            "1": "Food",
            "2": "Transport",
            "3": "Education",
            "4": "Entertainment",
            "5": "Shopping",
            "6": "Other"
        }

        category = categories.get(category_choice, "Other")

        try:
            amount = float(amount)

            if amount < 0:
                print("❌ Amount cannot be negative.")
                continue

            expense = {
                "name": name,
                "amount": amount,
                "category": category
            }

            expenses.append(expense)

            with open("expenses.txt", "a") as file:
                file.write(f"{name}|{amount}|{category}\n")

            print("✅ Expense added and saved successfully!")

        except ValueError:
            print("❌ Please enter a valid number.")

    elif choice == "2":
        if not expenses:
            print("\n📭 No expenses recorded yet.")
        else:
            print("\n📋 Your Expenses:")
            print("-----------------")

            for expense in expenses:
                print(
                    f"{expense['name']} | "
                    f"{expense['category']} | "
                    f"₹{expense['amount']:.2f}"
                )

    elif choice == "3":
        total = sum(expense["amount"] for expense in expenses)

        print(f"\n💰 Total spending: ₹{total:.2f}")

    elif choice == "4":
        print("👋 Thanks for using Student Expense Tracker!")
        break

    else:
        print("❌ Invalid choice. Please select 1-4.")

