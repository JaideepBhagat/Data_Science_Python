tasks = ["Buy Milk", "Attend meeting at 10 AM", "Call Umesh"]


def readFile():
    with open("TaskList.txt", 'r') as file:
        print(file.read())


with open("TaskList.txt", 'w') as file:
    for task in tasks:
        file.write(task+"\n")

readFile()

with open("TaskList.txt", 'a') as file:
    file.write("Go for a walk\n")

readFile()
