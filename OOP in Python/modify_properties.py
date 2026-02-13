class Person:
  def __init__(self, name='Ovi', age=18):
    self.name = name
    self.age = age


p1 = Person("John", 36)
print(p1.name, p1.age)

p2 = Person("Fx")
print(p2.name,p2.age)


p3 = Person()
print(p3.name,p3.age)

p4=Person()
p4.name='Ovon'
p4.age=27

print(p4.name,p4.age)