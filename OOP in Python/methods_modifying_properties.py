# Methods Modifying Properties


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birthday(self):
        self.age += 1
        print(f"Happy Birthday! You are now {self.age}")


p1 = Person("Ovi", 27)
p1.birthday()
p1.birthday()
p1.birthday()
p1.birthday()

p2 = Person("Ovi", 17)
p2.birthday()
p2.birthday()
