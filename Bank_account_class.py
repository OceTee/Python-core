# Object oriented Programming in Python
class BankAccount:
    """A simple Bank Account class to manage deposits and withdrawals."""
    def __init__(self, account_number, balance = 0): # Initialize the account with an account number and an optional balance
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):  # Method to deposit money into the account#
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):  # Method to withdraw money from the account
        # Check if the withdrawal amount is positive and does not exceed the current balance
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        else:
            print("Withdrawal amount must be positive and less than or equal to the current balance.")
    def get_balance(self):  # Method to get the current balance of the account
        return self.balance
    def __str__(self):  # String representation of the account
        return f"BankAccount(account_number={self.account_number}, balance={self.balance})"
    
# Example usage
if __name__ == "__main__": 
    account = BankAccount("123456789")
    print(account)  # Output: BankAccount(account_number=123456789, balance=0)
    account.deposit(100)  # Output: Deposited 100. New balance is 100.
    account.withdraw(50)   # Output: Withdrew 50. New balance is 50.
    print(account.get_balance())  # Output: 50
    account.withdraw(60)   # Output: Withdrawal amount must be positive and less than or equal to the current balance.
    account.deposit(-20)  # Output: Deposit amount must be positive.
    print(account)  # Output: BankAccount(account_number=123456789, balance=50)
    account.withdraw(50)   # Output: Withdrew 50. New balance is 0.
    print(account.get_balance())  # Output: 0

# BankAccount class for managing bank accounts with deposit and withdrawal functionality.