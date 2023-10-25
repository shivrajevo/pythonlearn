# method overriding:
class animal:
    def sound(self):
        print("no sound")


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

    def fullfun(self):
        super().sound()
        self.sound()


obj = crow()

obj.fullfun()
