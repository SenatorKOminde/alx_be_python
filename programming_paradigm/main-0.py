from bank_account import BankAccount

def main():
    account = BankAccount(250)
    account.deposit(67.0)
    account.withdraw(50.0)
    account.withdraw(300.0)  # This should trigger "Insufficient funds."
    account.display_balance()

if __name__ == "__main__":
    main()

