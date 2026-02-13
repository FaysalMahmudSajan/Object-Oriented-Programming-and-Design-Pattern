class Person:
    def __init__(self, name, age, title):
        self.name = name
        self.age = age
        self.title = title

    def person_info(self):
        print(
            f"\nHi, my name is {self.name}. I'm {self.age} years old. I'm a {self.title}."
        )


class Find_Person:
    def __init__(self, contact_number, address):
        self.contact_number = contact_number
        self.address = address

    def address_info(self):
        print (f"I'm from {self.address}. And my contact number is {self.contact_number}")


person_1 = Person("Ovi", 27, "Software Engineer")
person_1.person_info()
person_1=Find_Person('0140*********','Tongi')
person_1.address_info()

person_2 = Person("Abir", 22, "Data Analysis")
person_2.person_info()
person_2=Find_Person('0170*********','Mirpur')
person_2.address_info()
