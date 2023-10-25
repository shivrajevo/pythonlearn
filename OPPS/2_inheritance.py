# the class keyword
class parent:
    name = ""
    Class = 0

    def __init__(self, name, Class):
        self.name = name
        self.Class = Class

    def inputname(self):
        self.name = input("enter your name:")
        self.Class = int(input("enter your class"))

    def getdetails(self):
        print("your name is ", self.name)
        print("your class is ", self.Class)


class child(parent):
    def __init__(self, name, Class, grade):
        super().__init__(name, Class)
        self.grade = grade


obj = child("shivraj", 9, "A")

obj.getdetails()
