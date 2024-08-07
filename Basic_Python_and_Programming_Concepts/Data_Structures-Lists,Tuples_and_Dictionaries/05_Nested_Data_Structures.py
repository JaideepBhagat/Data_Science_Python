# List of Dictionaries
users = [
    {"name": "Jaideep Bhagat", "address": "Kharghar, Navi Mumbai, India"},
    {"name": "Swati Bhagat", "address": "Ravet, Pune, India"},
    {"name": "Suresh Bhagat", "address": "Roha, Raigad, India"},
]

# Printing the list
print(users)

# Accessing nested data
for user in users:
    print(f"{user['name']} lives at {user['address']}")
