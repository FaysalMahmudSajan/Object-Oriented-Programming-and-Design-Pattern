class A:
    def __init__(self, x):
        self.__x = x  # private property

    def get_x(self):
        return self.__x

a = A(25)
print(a.get_x())