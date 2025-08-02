class BankAccount:
    def __init__(self, starting_balance):
        self.account_balance = float(starting_balance)

    def deposit(self, amount):
        self.account_balance += amount
        print(f"Deposited: ${amount:.1f}")

    def withdraw(self, amount):
        if amount > self.account_balance:
            print("Insufficient funds.")
        else:
            self.account_balance -= amount
            print(f"Withdrew: ${amount:.1f}")

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")
