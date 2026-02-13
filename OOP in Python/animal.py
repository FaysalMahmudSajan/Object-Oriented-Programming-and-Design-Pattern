class Dog:
    def __init__(self):
        self.name = "Tommy"
        self.age = 5
        self.food = 'meat'
    def bark(self):
        print("Gaww Gaww")


dog_1 = Dog()
print(dog_1.name)
dog_1.bark()

dog_2 = Dog()
print(dog_2.food,dog_2.age)
dog_2.bark()