class Person:
    def __init__(self,name,salary):
        self.name=name
        self._salary=salary

p1 = Person('Ovi',65000)
print(p1.name,p1._salary)