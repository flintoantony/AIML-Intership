# Global storage
transactions = []
TAX_RATE = 0.1


def add_transaction(amount, t_type, category="General"):
    """Add a single transaction with a default category."""
    if not isinstance(amount, (int, float)) or amount <= 0:
        return "Invalid amount"

    if t_type not in ["income", "expense"]:
        return "Invalid transaction type"

    txn = {
        "amount": amount,
        "type": t_type,
        "category": category
    }

    transactions.append(txn)
    return txn


def bulk_add_expenses(*amounts, category):
    """Add multiple expenses using *args."""
    added = []
    for amt in amounts:
        if isinstance(amt, (int, float)) and amt > 0:
            added.append(add_transaction(amt, "expense", category))
    return added


def get_summary():
    """Return total income, total expenses, and net balance."""
    income = 0
    expense = 0

    for txn in transactions:
        if txn["type"] == "income":
            income += txn["amount"]
        else:
            expense += txn["amount"]

    return income, expense, income - expense


def calculate_tax(income):
    """Calculate tax using global TAX_RATE."""
    return income * TAX_RATE


def reset_tax_rate(new_rate):
    """Update the global TAX_RATE."""
    global TAX_RATE
    if 0 <= new_rate <= 1:
        TAX_RATE = new_rate
        return TAX_RATE
    return "Invalid tax rate"


def filter_transactions(predicate):
    """Return transactions that satisfy a condition function."""
    result = []
    for txn in transactions:
        if predicate(txn):
            result.append(txn)
    return result


def make_category_filter(category):
    """Return a function that filters transactions by category (closure)."""
    def filter_func(txn):
        return txn["category"] == category
    return filter_func


def compound_growth(principal, rate, years):
    """Recursively calculate compound growth."""
    if years == 0:
        return principal
    return compound_growth(principal * (1 + rate), rate, years - 1)


# Lambda functions
format_currency = lambda x: f"${x:,.2f}"
label_transaction = lambda t: f"{t['type'].upper()} | {t['category']} | {format_currency(t['amount'])}"


# BONUS: Budget checker closure
def make_budget_checker(limit):
    """Warn when expenses exceed a budget limit."""
    total = 0

    def checker(amount):
        nonlocal total
        total += amount
        if total > limit:
            return f"⚠ Budget exceeded! Total: {format_currency(total)}"
        return f"Within budget: {format_currency(total)}"
    return checker


# BONUS: Apply function to all
def apply_to_all(func, data):
    """Apply a function to all items in a list."""
    return [func(item) for item in data]


def main():
    """Main menu-driven program."""
    budget_checker = make_budget_checker(5000)

    while True:
        print("\n===== PERSONAL FINANCE TRACKER =====")
        print("1. Add Transaction")
        print("2. Bulk Add Expenses")
        print("3. View Summary")
        print("4. Filter by Category")
        print("5. Calculate Tax")
        print("6. Compound Growth")
        print("7. Show All Transactions")
        print("8. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            try:
                amt = float(input("Amount: "))
                t_type = input("Type (income/expense): ")
                cat = input("Category (optional): ")

                if cat.strip() == "":
                    txn = add_transaction(amt, t_type)
                else:
                    txn = add_transaction(amt, t_type, cat)

                print("Added:", txn)

                if t_type == "expense":
                    print(budget_checker(amt))

            except:
                print("Invalid input!")

        elif choice == "2":
            try:
                values = input("Enter expenses separated by space: ").split()
                values = [float(v) for v in values]
                cat = input("Category: ")
                print(bulk_add_expenses(*values, category=cat))
            except:
                print("Invalid input!")

        elif choice == "3":
            inc, exp, bal = get_summary()
            print("Income:", format_currency(inc))
            print("Expenses:", format_currency(exp))
            print("Balance:", format_currency(bal))

        elif choice == "4":
            cat = input("Enter category: ")
            cat_filter = make_category_filter(cat)
            filtered = filter_transactions(cat_filter)
            print(apply_to_all(label_transaction, filtered))

        elif choice == "5":
            inc, _, _ = get_summary()
            print("Tax:", format_currency(calculate_tax(inc)))

        elif choice == "6":
            try:
                p = float(input("Principal: "))
                r = float(input("Rate (0-1): "))
                y = int(input("Years: "))
                print("Future Value:", format_currency(compound_growth(p, r, y)))
            except:
                print("Invalid input!")

        elif choice == "7":
            print(apply_to_all(label_transaction, transactions))

        elif choice == "8":
            print("Exiting...")
            break

        else:
            print("Invalid choice!")


# Run program
main()