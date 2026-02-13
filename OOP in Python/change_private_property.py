class A:
    def __init__(self, x):
        self.__x = x

    def get_value(self):
        return self.__x

    def set_value(self, x):
        self.__x = x


a = A(25)
print(a.get_value())
a.set_value(30)
print(a.get_value())