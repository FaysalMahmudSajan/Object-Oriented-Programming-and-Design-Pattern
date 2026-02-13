class Outer:
    def __init__(self):
        self.name="Outer class"
    
    class Inner:
        def __init__(self):
            self.name="Inner class"
        

c=Outer()
print(c.name)
c1=c.Inner()
print(c1.name)