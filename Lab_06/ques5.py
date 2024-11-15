# Write a program to define a class to represent a bank account, with methods to deposit, withdraw, and check the balance. in python

class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Rs{amount} deposited. New balance: Rs{self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Rs{amount} withdrawn. New balance: Rs{self.balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        print(f"Current balance: Rs{self.balance}")

account = BankAccount("Alice", 100)
account.check_balance()   
account.deposit(50)       
account.withdraw(30)      
account.check_balance()   
