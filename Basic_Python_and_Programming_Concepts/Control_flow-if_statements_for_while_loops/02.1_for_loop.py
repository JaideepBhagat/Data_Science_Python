# multiplication table using a for loop
number = int(input("Enter the number for multiplication table\n"))

for i in range(1, 10):
    print(f"{number} x {i} = {number * i}")
