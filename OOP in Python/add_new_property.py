class Person:
    species = "human"  # class property

    def __init__(self, name):  # instance property
        self.name = name


p1 = Person('')
a = p1.name = "Jhon" # change name
b = p1.age = 36 # add new property
c = p1.species = "Monkey" # change class property
print(a, b, c)
