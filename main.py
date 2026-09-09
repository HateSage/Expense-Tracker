import json


def add_expense(expenses):
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    description = input("Enter description: ")

    expense = {
        "amount": amount,
        "category": category,
        "description": description
    }

    expenses.append(expense)


def show_expenses(expenses):
    for i, expense in enumerate(expenses, start=1):
        print(
            i,
            expense["amount"],
            expense["category"],
            expense["description"]
        )


def total_expenses(expenses):
    total = 0

    for expense in expenses:
        total = total + expense["amount"]

    return total


def spending_by_category(expenses):
    spending = {}

    for expense in expenses:
        category = expense["category"]

        if category in spending:
            spending[category] = spending[category] + expense["amount"]
        else:
            spending[category] = expense["amount"]

    return spending


def delete_expense(expenses):
    show_expenses(expenses)

    choice = int(input("Which expense do you want to delete? "))
    choice -= 1

    del expenses[choice]


def save_expenses(expenses):
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)


def load_expenses():
    try:
        with open("expenses.json", "r") as file:
            expenses = json.load(file)

        return expenses

    except FileNotFoundError:
        return []


def main():
    expenses = load_expenses()

    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add expense")
        print("2. View expenses")
        print("3. Total spending")
        print("4. Spending by category")
        print("5. Delete expense")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense(expenses)
            save_expenses(expenses)

        elif choice == "2":
            show_expenses(expenses)

        elif choice == "3":
            print("Total spending:", total_expenses(expenses))

        elif choice == "4":
            spending = spending_by_category(expenses)

            for category, amount in spending.items():
                print(category, ":", amount)

        elif choice == "5":
            delete_expense(expenses)
            save_expenses(expenses)
            print("Deleted Successfully")

        elif choice == "6":
            save_expenses(expenses)
            print("Goodbye!")
            break

        else:
            print("Invalid option.")

main()


