my_list = [1, 2, 3, 'a', 'b', 'c']
# Iterating over a list
for item in my_list:
    print(item)

my_tuple = tuple(my_list)
# Iterating over a tuple
for item in my_tuple:
    print(item)

# Iterating over a dictionary
my_dict = {1:'a',2:'b',3:'c'}
for key, value in my_dict.items():
    print(f"{key}: {value}")
