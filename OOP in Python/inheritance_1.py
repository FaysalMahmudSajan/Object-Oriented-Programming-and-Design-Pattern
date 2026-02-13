class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        return (self.fname, self.lname)


class Student(Person):
    def __init__(self, fname, lname, graduationyear):
        super().__init__(fname, lname)
        self.graduationyear = graduationyear


x = Student("Nazmul", "Hassan", 2026)
print(x.printname())
print(x.graduationyear)
