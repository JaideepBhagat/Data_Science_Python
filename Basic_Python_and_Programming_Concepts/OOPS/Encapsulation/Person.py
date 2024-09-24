class Person:
    def __init__(self, name, age):
        self.name = name            # Public
        self._age = age             # Protected
        self.__secret = "My secret" # Private

    # Getter method to expose protected variable
    def get_age(self):
        return self._age

    # Setter method to set protected variable
    def set_age(self, age):
        if age < 0:
            raise ValueError("Age cannot be negative")
        else:
            self._age = age


    # Getter method to expose private variable
    @property
    def secret(self):
        return self.__secret


    # Setter method to set private variable
    @secret.setter
    def secret(self, message):
        self.__secret = message
