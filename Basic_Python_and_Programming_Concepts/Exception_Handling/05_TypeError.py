try:
    num1 = input("Number 1: ")
    num2 = input("Number 2: ")
    div = num1/num2
    print(div)
except TypeError as e:
    print("Error: cannot process arithmetic operations on string data")
