import sys
from bank_account import BankAccount

def main():
    # Initialize account with $100 (can be adjusted for testing)
    account = BankAccount(100)

    # Check if command-line argument is provided
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    # Parse command and optional amount
    try:
        command_part = sys.argv[1]
        if ':' in command_part:
            command, amount_str = command_part.split(':', 1)
            amount = float(amount_str)
        else:
            command = command_part
            amount = None

        # Execute based on command
        if command == "deposit" and amount is not None:
            account.deposit(amount)
            print(f"Deposited: ${amount:.2f}")
        elif command == "withdraw" and amount is not None:
            if account.withdraw(amount):
                print(f"Withdrew: ${amount:.2f}")
            else:
                print("Insufficient funds.")
        elif command == "display":
            account.display_balance()
        else:
            print("Invalid command.")
            print("Valid commands: deposit:<amount>, withdraw:<amount>, display")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()