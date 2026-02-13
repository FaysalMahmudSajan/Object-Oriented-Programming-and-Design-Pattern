class A:
    def __init__(self, x):
        self.__x = x  # private property

a = A(25)
print(a.__x)  # This will cause an error