def check_age(age):
    if age <= 18:
        raise ValueError("Age must be at least 18")
    else:
        return True

try:
    age = int(input("Enter your age: "))
    if check_age(age):
        print("You are eligible for voting")
except ValueError as e:
    print(e)
