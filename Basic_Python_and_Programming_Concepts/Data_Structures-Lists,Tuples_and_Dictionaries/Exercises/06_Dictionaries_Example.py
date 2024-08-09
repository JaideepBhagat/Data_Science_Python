student = {
    'name': 'John',
    'age': 22,
    'major': 'Computer Science'
}
print(student)  # Output: {'name': 'John', 'age': 22, 'major': 'Computer Science'}

# Adding a new key-value pair
student['email'] = 'john@example.com'
print(student)  # Output: {'name': 'John', 'age': 22, 'major': 'Computer Science', 'email': 'john@example.com'}

# Modifying an existing value
student['age'] = 23
print(student)  # Output: {'name': 'John', 'age': 23, 'major': 'Computer Science', 'email': 'john@example.com'}

# Removing a key-value pair
del student['major']
print(student)  # Output: {'name': 'John', 'age': 23, 'email': 'john@example.com'}
