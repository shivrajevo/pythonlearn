# method overloading:
class animal:
    def sound(self):
        pass


class dog(animal):
    def sound(self):
        print("dog : wolf - wolf")


class cat(animal):
    def sound(self):
        print("cat : meaooo")


class rat(animal):
    def sound(self):
        print("rat : chew chew")


class crow(animal):
    def sound(self):
        print("crow : ca-oo ca-oo")


obj = dog()

obj.sound()



manveer is good boy
