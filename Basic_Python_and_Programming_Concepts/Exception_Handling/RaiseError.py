def check_age(age):
    if age < 18:
        raise ValueError("Age must be at least 18")


try:
    check_age(16)
except ValueError as e:
    print(e)
