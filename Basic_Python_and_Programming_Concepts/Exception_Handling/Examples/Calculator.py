def calculator():
    try:
        num1 = float(input("Enter the first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter the second number: "))

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            result = num1 / num2
        # else:
        #     return "Error: Invalid Operator"

        return f"Result: {result}"

    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    except ValueError:
        return "Error: Invalid Input. Please enter a number"
    except Exception as e:
        return f"An unexpected error occurred: {e}"


print(calculator())
