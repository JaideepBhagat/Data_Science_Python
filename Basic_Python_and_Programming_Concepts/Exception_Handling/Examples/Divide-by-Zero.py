def divide_numbers(numerator, denominator):
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    else:
        return f"Result: {result}"


print(divide_numbers(int(input("Enter Numerator: ")),int(input("Enter Denominator: "))))
