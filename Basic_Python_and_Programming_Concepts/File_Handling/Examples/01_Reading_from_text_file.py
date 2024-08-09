# Assume we have a log file named log.txt

try:
    with open("log.txt",'r') as file:
        content = file.read()
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        print(content)
except FileNotFoundError:
    print("Log file not found")
