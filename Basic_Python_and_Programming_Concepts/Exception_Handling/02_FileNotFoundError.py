try:
    import os

    file_path = "C:\\Data\\my_file.txt"  # This is the file path you provided
    file_name = os.path.splitext(os.path.basename(file_path))[0]
    file = open(file_path,'r')
except FileNotFoundError:
    print(f"{file_name} was not found")