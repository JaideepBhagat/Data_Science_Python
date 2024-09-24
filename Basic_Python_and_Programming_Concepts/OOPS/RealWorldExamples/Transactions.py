from BankAccount import BankAccount
from SavingAccount import SavingAccount
from CurrentAccount import CurrentAccount

# Creating a generic Bank account
generic_account = BankAccount("Jaideep Bhagat", 10000)
generic_account.get_account_statement()
generic_account.deposit(5000)
generic_account.withdraw(2000)


# Creating a Saving Account
print("\n")
savings_account = SavingAccount("Swati", 10000, 0.05)
savings_account.get_account_statement()
savings_account.add_interest()
savings_account.withdraw(2000)
savings_account.get_account_statement()

# Creating a Current Account
print("\n")
current_account = CurrentAccount("Aaryan Enterprises", 10000, 5000)
current_account.get_account_statement()
current_account.withdraw(2000)
current_account.withdraw(10000)
