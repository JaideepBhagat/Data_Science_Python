try:
    number = int(input("Enter a number:"))
    result = 100/number
except ValueError:
    print("That's not a valid number.")
except ZeroDivisionError:
    print("Cannot divide by Zero")
