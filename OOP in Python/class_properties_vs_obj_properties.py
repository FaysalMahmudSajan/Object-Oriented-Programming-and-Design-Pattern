class Person:
    species="human" # class property
    def __init__(self, name, age): # instance property
        self.name = name 
        self.age = age
    def run(self):
        self.name
        print(self.name,self.age)
      

p1=Person("Jhon",36)
print(p1.name,p1.age,p1.species)

