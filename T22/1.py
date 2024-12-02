
# You are given a list of transactions where each transaction is represented by a dictionary containing date, amount, and type (either "debit" or "credit"). Write a Python function to calculate the total balance after all transactions. The initial balance is 0.

def transactions_amount(transactions):

    balance=0

    for  transaction in transactions:

        if transaction["type"] == "credit":

            balance +=  transaction["amount"]

        elif transaction["type"] == "debit":

            balance -=  transaction["amount"]

    return  balance


transactions = [
    {"date": "2024-07-01", "amount": 100.0, "type": "credit"},
    {"date": "2024-07-02", "amount": 50.0, "type": "debit"},
    {"date": "2024-07-03", "amount": 200.0, "type": "credit"},
    {"date": "2024-07-04", "amount": 30.0, "type": "debit"}
]

print(transactions_amount(transactions))