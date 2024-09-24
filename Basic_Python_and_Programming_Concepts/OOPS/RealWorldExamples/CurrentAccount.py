from BankAccount import BankAccount

class CurrentAccount(BankAccount):
    def __init__(self, account_holder, balance, overdraft_limit = 500):
        super().__init__(account_holder, balance)
        self.overdraft_limit = overdraft_limit

    # Overriding withdraw method for overdraft functionality
    def withdraw(self, amount):
        if 0 < amount <= (self.balance + self.overdraft_limit):
            self.balance -= amount
            print(f"Withdrawn: {amount}. New Balance is {self.balance}")
        else:
            print("Invalid Withdrawal amount or Exceeded Overdraft Limit")

    @staticmethod
    def account_type(self):
        return "Current Account"
