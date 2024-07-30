# Compound Interest Calculation
principal = int(input("Enter the initial amount: "))
rate = float(input("Enter the annual interest rate: "))
time = int(input("Enter the time period in years: "))

# Compound Interest formula A  = P(1+r/n)^nt
amount = principal * (1 + rate / 100) ** time
print(f"Future value of the investment: {amount:.2f}")
