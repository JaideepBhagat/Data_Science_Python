# Creating a list
my_list = [1, 2, 3, 'a', 'b', 'c']

# Accessing elements
print(my_list[0])  # Output: 1

# Modifying elements
my_list[1] = 'new_value'

# Adding elements
my_list.append('new_item')

# Removing elements
my_list.remove('a')

# Slicing
print(my_list[1:3])  # Output: ['new_value', 3]

# Iterating through a list
for item in my_list:
    print(item)
