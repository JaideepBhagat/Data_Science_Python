from Parent import Parent

class Child(Parent):
    def play(self):
        print(f"{self.name} is playing")

    # Overriding methods from the parent class
    def greet(self):
        super().greet()  # Calls the parent class Greet method
        print(f"I am a child")
