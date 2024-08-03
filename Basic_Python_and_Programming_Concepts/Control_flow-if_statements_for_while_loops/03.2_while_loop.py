# Asking for a valid password
password = ""

while password != "Bond_007":
    password = input("Enter the password: ")
    if password == "Bond_007":
        print("Access granted.")
    else:
        print("Incorrect password, try again.")
