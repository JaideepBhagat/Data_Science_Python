import random

class BankAccount:
    # Class variable to store all account numbers
    all_account_numbers = set()

    def __init__(self, account_holder, balance = 0):
        self.account_holder = account_holder
        self._balance = balance
        self.__account_number = self.__generate_unique_account_number()

    # Property decorator to get account balance
    @property
    def balance(self):
        return self._balance

    # Property decorator with setter to modify the balance
    @balance.setter
    def balance(self, amount):
            self._balance = amount

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited: {amount}. New Balance is {self.balance}")
        else:
            print("Deposited amount must be positive")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self.balance -= amount # Using the property setter
            print(f"Withdrawn: {amount}. New Balance is {self.balance}")
        else:
            print("Invalid Withdrawal amount or Insufficient Balance")

    # Private method to generate a unique 12 digit account number
    def __generate_unique_account_number(self):
        while True:
            # Generate a random 12 digit account number as a string
            new_account_number = str(random.randint(100000000000, 999999999999))
            # Check if the generated account number is unique
            if new_account_number not in self.all_account_numbers:
                self.all_account_numbers.add(new_account_number)
                return new_account_number

    # Property decorator to access the private account number
    @property
    def account_number(self):
        return self.__account_number

    # Public method to get the account statement
    def get_account_statement(self):
        print(f"Account Statement for {self.account_holder}: \n\tAccount Number: {self.account_number}\n\tBalance: {self.balance}")
