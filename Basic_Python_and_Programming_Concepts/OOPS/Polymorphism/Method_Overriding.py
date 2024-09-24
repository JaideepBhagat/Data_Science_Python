class Animal:
    def speak(self):
        print("The animal makes a sound")


class Dog(Animal):
    def speak(self):
        print("The dog barks")

myAnimal = Animal()
myAnimal.speak()
print("-----")
myDog = Dog()
myDog.speak()
