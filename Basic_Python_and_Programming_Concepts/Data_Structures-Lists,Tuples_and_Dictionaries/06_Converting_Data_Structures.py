# Converting list to tuple
users = ["Jaideep", "Swati", "Suresh"]
users_tuple = tuple(users)
print(users_tuple)

# Converting tuple to list
new_list = list(users_tuple)
print(new_list)

# Creating a dictionary from two lists
keys = ["name", "address"]
values = ["Jaideep Bhagat", "Kharghar, Navi Mumbai, India"]
user = dict(zip(keys, values))
print(user)