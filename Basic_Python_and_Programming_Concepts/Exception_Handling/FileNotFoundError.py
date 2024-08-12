try:
    file = open("my_file.txt",'r')
except FileNotFoundError:
    print("Error: Mentioned file was not found.")
