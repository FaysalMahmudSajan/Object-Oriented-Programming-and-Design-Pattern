class Person:
    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary

p1 = Person('Ovi',65000)
print(p1.name,p1.__salary)


# ---------------------------------------------------------------------------
# AttributeError                            Traceback (most recent call last)
# Cell In[4], line 7
#       4         self.__salary=salary
#       6 p1 = Person('Ovi',65000)
# ----> 7 print(p1.name,p1.__salary)

# AttributeError: 'Person' object has no attribute '__salary'