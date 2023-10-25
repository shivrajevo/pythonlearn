class A:
    def __init__(self, name):
        self.name = name


class B:
    def __init__(self, Class):
        self.Class = Class


class both(A, B):
    def __init__(self, name, Class):
        A.__init__(self, name)
        B.__init__(self, Class)

    def printdetails(self):
        print(self.name)
        print(self.Class)


obj = both("shivraj", 9)
obj.printdetails()
