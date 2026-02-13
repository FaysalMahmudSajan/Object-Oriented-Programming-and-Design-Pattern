class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(f"My full name is {self.fname} {self.lname}.")


class Student(Person):
    def __init__(self, fname, lname, grade):
        super().__init__(fname, lname)
        self.grade = grade
        print(self.grade)


s1 = Student("Nazmul", "Hassan",3.4)
s1.printname()


s1 = Student("Nazmul", "Hassan")
s1.printname()
