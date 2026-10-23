#python
# ATM Transaction Sequence Simulation

balance = 5000
withdrawal_limit = 2000

total_deposits = 0
total_withdrawals = 0
successful_transactions = 0
rejected_transactions = 0

print("===== ATM TRANSACTION SYSTEM =====")
print("Initial Balance: Rs.", balance)

n = int(input("Enter the number of transactions: "))

for i in range(n):
    print("\nTransaction", i + 1)
    print("1. Deposit")
    print("2. Withdraw")

    choice = int(input("Enter your choice: "))
    amount = float(input("Enter amount: "))

    if amount <= 0:
        print("Invalid amount! Transaction rejected.")
        rejected_transactions += 1

    elif choice == 1:
        balance += amount
        total_deposits += amount
        successful_transactions += 1
        print("Deposit successful.")

    elif choice == 2:
        if amount > withdrawal_limit:
            print("Transaction rejected! Withdrawal limit exceeded.")
            rejected_transactions += 1

        elif amount > balance:
            print("Transaction rejected! Insufficient balance.")
            rejected_transactions += 1

        else:
            balance -= amount
            total_withdrawals += amount
            successful_transactions += 1
            print("Withdrawal successful.")

    else:
        print("Invalid transaction choice.")
        rejected_transactions += 1

    print("Current Balance: Rs.", round(balance, 2))

print("\n===== TRANSACTION SUMMARY =====")
print("Initial Balance: Rs. 5000")
print("Total Deposits: Rs.", round(total_deposits, 2))
print("Total Withdrawals: Rs.", round(total_withdrawals, 2))
print("Successful Transactions:", successful_transactions)
print("Rejected Transactions:", rejected_transactions)
print("Final Balance: Rs.", round(balance, 2))
