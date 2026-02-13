class Person:
    def __init__(self, name, age, title):
        self.name = name
        self.age = age
        self.title = title

    def person_info(self):
        print(
            f"\nHi, my name is {self.name}. I'm {self.age} years old. I'm a {self.title}."
        )

person_1 = Person("Ovi", 27, "Software Engineer")
person_1.person_info()

del person_1

person_1.person_info()