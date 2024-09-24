from BankAccount import BankAccount

class SavingAccount(BankAccount):
    def __init__(self, account_holder, balance = 0, interest_rate = 0.02):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Added interest: {interest}. New Balance is {self.balance}")

    def account_type(self):
        return "Savings Account"
