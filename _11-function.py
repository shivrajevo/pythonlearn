# A function is a block of code that performs a task.
# It can be called and reused multiple times.
# You can pass information to a function and it can send information back

# ------------------------------------ syntax to create a function

# def <-- keyword use to create a function (in python)*


def myname():
    print("shivraj singh is my name")


myname()  # function calling

# if you make a function you can call it many time in function

# for example

for i in range(1, 10 + 1):
    myname()

# -------------------------------------- pass value to function


def add(a, b):
    print(a + b)


add(10, 20)


# -------------------------------------- return value

# return statement is work similar as break in loop it treminate the function block exe.

# A parameter is the variable listed inside the parentheses in the function definition.


def findmax(a, b):
    if a > b:
        return a
    else:
        return b


a = findmax(100, 20)
# An argument is the value that is sent to the function when it is called.

# print(type(a))

# print(findmax(100, 20))

# ---------------------------------------- pass by value and pass by reference
