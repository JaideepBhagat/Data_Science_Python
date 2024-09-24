from Person import Person

p1 = Person("Jaideep", 42)

print(p1.name)
p1.name = "Swati"
print(p1.name)
print("------------------------")
print(p1.age())
p1.set_age(40)
print("------------------------")
print(p1.secret)
p1.secret = "My new secret"
print(p1.secret)
