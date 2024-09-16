import json

transactions = []

def display_menu():
    print("\nPersonal Finance Manager:")
    print("1. Add a new Transaction")
    print("2. View Transactions")
    print("3. View Summary")
    print("4. Search for a Transaction")
    print("5. Save data to a file")
    print("6. Load data from a file")
    print("7. Exit")

def add_transactions():
    date = input("Enter date in (YYYY-MM-DD) : ")
    description = input("Enter description : ")
    amount = float(input("Enter amount : "))
    type_ = input("Type (income/expense) : ").lower()

    single_transaction = {
        'date': date,
        'description': description,
        'amount': amount,
        'type': type_
    }

    transactions.append(single_transaction)

def view_transactions():
    start_date = input("Enter Start date (YYYY-MM-DD) or press Enter to view all: ")
    end_date = input("Enter End date (YYYY-MM-DD) or press Enter to view all: ")

    for transaction in transactions:
        if start_date and end_date:
            if start_date <= transaction['date'] <= end_date:
                print(transaction)
        else:
            print(transaction)
        
def view_summary():
    total_income = sum(t['amount'] for t in transactions if t['type'] == "income")
    total_expense = sum(t['amount'] for t in transactions if t['type'] == "expense")
    total_savings = total_income - total_expense

    print("-----SUMMARY-----")
    print(f"Total Income: {total_income} /-")
    print(f"Total Expense: {total_expense} /-")
    print(f"Total Savings: {total_savings} /-")

def search_transactions():
    user_input = input("Enter description or amount of the transaction: ")

    found = False
    for transaction in transactions:
        # Try converting user_input to float
        try:
            user_amount = float(user_input)
            # Check if the amount matches
            if user_amount == transaction['amount']:
                print(transaction)
                found = True
        except ValueError:
            # Handle case where user_input is not a number
            if user_input.lower() in transaction['description'].lower():
                print(transaction)
                found = True

    if not found:
        print("Transaction not found")


def save_data():
    file_name = input("Enter the name of file: ")

    with open(file_name, 'w') as file:
        json.dump(transactions, file, indent=4)

    print("Data saved successfully")

def load_data():
    file_name = input("Enter the filename to load data: ")

    with open(file_name, 'r') as file:
        global transactions
        transactions = json.load(file)

    print("Data loaded successfully")
