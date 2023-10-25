# the class keyword
class person:
    # there are the member of our class
    name = ""
    Class = 0

    # there are methods of our class

    # self is important because object is passed in method
    def inputname(self):
        self.name = input("enter your name:")
        self.Class = int(input("enter your class"))

    def getdetails(self):
        print("your name is ", self.name)
        print("your class is ", self.Class)


# you can create multiple object using class
obj1 = person()
obj2 = person()

obj1.inputname()
obj1.getdetails()
