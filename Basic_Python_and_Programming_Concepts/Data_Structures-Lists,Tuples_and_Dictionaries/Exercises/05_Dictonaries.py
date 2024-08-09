# Creating a dictionary
my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}

# Accessing values
print(my_dict['name'])  # Output: Alice

# Modifying values
my_dict['age'] = 26

# Adding key-value pairs
my_dict['email'] = 'alice@example.com'

# Removing key-value pairs
del my_dict['city']

# Iterating through keys and values
for key, value in my_dict.items():
    print(f"{key}: {value}")
