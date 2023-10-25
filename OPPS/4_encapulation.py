# member hiding / data hiding


class A:
    def __init__(self, name, mobile, password):
        # a normal variable
        self.normalmember = name
        # a protected variable
        self._protected = mobile
        # name mangling
        self.__private = password


class B(A):
    def getdata(self):
        print(self.normalmember)
        print(self.__private)


obj = A("shivraj", 902735072, "880sk87sl")

print(obj._A__private)
