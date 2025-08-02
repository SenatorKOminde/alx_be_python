class BankAccount:
    def __init__(self, starting_balance):
        if starting_balance < 0:
            raise ValueError("Starting balance cannot be negative.")
        self.account_balance = float(starting_balance)

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.account_balance += amount
        print(f"Deposited: ${amount:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.account_balance:
            print("Insufficient funds.")
        else:
            self.account_balance -= amount
            print(f"Withdrew: ${amount:.2f}")

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")


