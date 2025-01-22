class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of {amount} added to your balance. New balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawal of {amount} processed. New balance: {self.balance}")
        else:
            print("Insufficient funds")

print("Welcome to our bank")
initial_balance = int(input("Enter initial balance: "))
account = BankAccount(initial_balance)

while True:
    print("\nChoose an option:")
    print("1 for deposit")
    print("2 for withdraw")
    print("3 for exit")
    option = int(input())

    if option == 1:
        deposit_amount = int(input("Enter deposit amount: "))
        account.deposit(deposit_amount)
    elif option == 2:
        withdraw_amount = int(input("Enter withdrawal amount: "))
        account.withdraw(withdraw_amount)
    elif option == 3:
        print("Thank you for using our bank!")
        break
    else:
        print("Invalid option, please try again.")
