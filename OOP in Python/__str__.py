class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def __str__(self): 
        return f"{self.name} {self.age}"
    
p1=Person('Fx',26)
print(p1) # just call obj then get __str__ value