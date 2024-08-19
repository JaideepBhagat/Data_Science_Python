try:
    file = open("Sample.txt", 'r')
    content = file.read()
except FileNotFoundError:
    print("Error: File not found")
else:
    print("File read successfully")
finally:
    print("This will run no matter what")
