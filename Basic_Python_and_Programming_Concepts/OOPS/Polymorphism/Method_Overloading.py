class Calculator:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c=0):
        return a + b + c

calc = Calculator()
print(calc.add(1, 2))
print(calc.add(1, 2, 3))