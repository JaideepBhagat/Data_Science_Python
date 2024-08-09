try:
    file = open("Example.txt", 'w')  # Opens the file in write mode
    file.write("Hello Jaideep\nHow are you?\nHow is your family?")  # Writes content to the file

    file = open("Example.txt", 'r')  # Opens the file in read mode

    content = file.read()  # Reads entire content of the file
    line = file.readline()  # Reads one line from the file
    lines = file.readlines()  # Reads all lines into a list

    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print(content)
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print(line)
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print(lines)
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

except FileNotFoundError:
    print("The file you are trying to open, does not exist")
finally:
    file.close()  # Close the file even if an error occurs
