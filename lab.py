class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("Alice", 30)
person2 = Person("Julius", 19)
person3 = Person("John", 24)
print(f"{person1.name} is {person1.age} years old.")
print(f"{person2.name} is {person2.age} years old.")
print(f"{person3.name} is {person3.age} years old.")
