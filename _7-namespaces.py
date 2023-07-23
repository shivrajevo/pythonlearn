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
# at module level : ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'a', 'b', 'c', 'd', 'fun1', 'fun2']
fun1()
# level of fun1  ['a', 'b', 'c']
fun2()
# level of fun2  ['a', 'b', 'c', 'd']
