class BankAccount:
    """A simple bank account class to manage deposits, withdrawals, and balance display."""

    def __init__(self, initial_balance=0.0):
        """
        Initialize the bank account with an optional initial balance.
        
        :param initial_balance: Starting balance for the account (default is 0)
        """
        self._account_balance = initial_balance  # Encapsulated using single underscore

    def deposit(self, amount):
        """
        Deposit a specified amount into the account.
        
        :param amount: The amount to deposit (must be positive)
        """
        if amount > 0:
            self._account_balance += amount
        else:
            raise ValueError("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraw a specified amount from the account if sufficient funds exist.
        
        :param amount: The amount to withdraw
        :return: True if successful, False otherwise
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount <= self._account_balance:
            self._account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """
        Print the current account balance in a user-friendly format.
        """
        print(f"Current Balance: ${self._account_balance:.2f}")
