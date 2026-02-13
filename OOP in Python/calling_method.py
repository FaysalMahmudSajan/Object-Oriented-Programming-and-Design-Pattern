class DefaultValue:
    def __init__(self,name='Faysal',age=2):
        self.name=name
        self.age=age
    def person_name(self):
        return (f"Hi, my name is {self.name}.")
    def run(self):
        msg=self.person_name()
        print(f"{msg} I'm {self.age}")

obj=DefaultValue()
obj.run()

obj_1=DefaultValue('Ovi',27)
obj_1.run()