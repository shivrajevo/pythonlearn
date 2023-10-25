# the class keyword
class person:
    # there are the member of our class
    name = ""
    Class = 0

    # constructor is a function that call at creation of an object
    def __init__(self, name, Class):
        self.name = name
        self.Class = Class

    # there are methods of our class

    # self is important because object is passed in method
    def change_details(self):
        self.name = input("enter your name:")
        self.Class = int(input("enter your class"))

    def getdetails(self):
        print("your name is ", self.name)
        print("your class is ", self.Class)

    def rename(self, newname):
        self.name = newname


# you can create multiple object using class
obj1 = person("shiva", 5)
obj2 = person("grupreet", 8)

obj1.change_details()
obj1.getdetails()
