# Asking for a valid password
password = ""

while password != "secret":
    password = input("Enter the password: ")
    if password == "secret":
        print("Access granted.")
    else:
        print("Incorrect password, try again.")
