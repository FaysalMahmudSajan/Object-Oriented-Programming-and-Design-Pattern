class Car:
    def __init__(self,name,doing):
        self.name=name
        self.doing=doing

    def explain(self):
        print(f"{self.name} is {self.doing}")
        
class Ship:
    def __init__(self,name,doing):
        self.name=name
        self.doing=doing

    def explain(self):
        print(f"{self.name} is {self.doing}")
        

class Rocket:
    def __init__(self,name,doing):
        self.name=name
        self.doing=doing

    def explain(self):
        print(f"{self.name} is {self.doing}")
        


c=Car('BMW','Expensive')
s=Ship('Titanic',"Horror")
r=Rocket('SpaceX','Growing Fast')

for x in (c,s,r):
    x.explain()