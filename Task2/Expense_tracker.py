print("===== EXPENSE TRACKER =====")
print("Enter your expenses one by one.")
print("Type 'q' to finish.\n")

total = 0
count = 0

while True:
    expense = input("Enter expense (or 'q' to quit): ")

    if expense.lower() == 'q':
        break

    try:
        expense = float(expense)

        if expense < 0:
            print("Expense cannot be negative!")
            continue

        total += expense
        count += 1

        print(f"Expense Added: ₹{expense:.2f}")
        print(f"Current Total: ₹{total:.2f}\n")

    except ValueError:
        print("Invalid input! Please enter a valid number.\n")

print("\n===== EXPENSE SUMMARY =====")
print("Total Expenses Entered:", count)
print(f"Total Amount Spent: ₹{total:.2f}")
print("Thank you for using Expense Tracker!")