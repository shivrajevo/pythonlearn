# the namespace is created by python itself. it contain a record of all avalable object
# at different level it create a different namespace
# it also ensure to update the object with new initilization

a = 20
b = 20
c = 20
d = 30


def fun1():
    a = 20
    b = 20
    c = 20
    print("level of fun1 ", dir())


def fun2():
    a = 20
    b = 20
    c = 20
    d = 30
    print("level of fun2 ", dir())


print("at module level :", dir())
fun1()
fun2()
