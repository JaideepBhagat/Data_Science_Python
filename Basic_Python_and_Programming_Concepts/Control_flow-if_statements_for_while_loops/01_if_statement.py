user_role = input("Enter your role: ")

if user_role == "admin":
    print("Access granted with Admin rights")
elif user_role == "student" or user_role == "teacher":
    print("Limited access granted to the system")
else:
    print("Access Denied")
