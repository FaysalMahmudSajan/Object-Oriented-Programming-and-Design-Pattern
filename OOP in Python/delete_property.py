class Person:
    def __init__(self, name="Ovi", age=27):
        self.name = name
        self.age = age
    def run(self):
        self.name
        print(self.name,self.age)

    def run_1(self):
        self.name='Sami'
        print(self.name,self.age)
      

p1=Person("Jhon",36)
del p1.name
p1.run_1()
p1.run()

