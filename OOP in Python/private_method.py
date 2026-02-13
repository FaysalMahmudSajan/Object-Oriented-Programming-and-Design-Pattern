class Calculator:
    def __init__(self):
        self.result = 0

    def __validate(self,num):
        return isinstance(num,(int,float))
    
    def add(self,num):
        if self.__validate(num):
            self.result+=num
        else:
            print("invalid number")



calc=Calculator()
calc.add(10)
calc.add(5)
# calc.__validate(25)
print(calc.result)