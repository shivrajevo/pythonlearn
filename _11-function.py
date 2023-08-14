# # A function is a block of code that performs a task.
# # It can be called and reused multiple times.
# # You can pass information to a function and it can send information back also

# # ------------------------------------ syntax to create a function

# # def <-- keyword use to create a function (in python)*


# def myname():
#     print(" _your-name_ is my name")


# myname()  # function calling

# # if you make a function you can call it many time in function

# # for example

# for i in range(1, 10 + 1):
#     myname()

# # -------------------------------------- pass value to function

# # add parameters in functions

# def add(a, b):
#     print(a + b)


# add(10, 20)


# # -------------------------------------- return value

# # return statement is work similar as break in loop it treminate the function block exe.

# # A parameter is the variable listed inside the parentheses in the function definition.


# def findmax(a, b):
#     if a > b:
#         return a
#     else:
#         return b


# a = findmax(100, 20)
# # An argument is the value that is sent to the function when it is called.

# # print(type(a))

# # print(findmax(100, 20))

# # --> if you dont need how many arguments add to function so you can use *args
# # Arbitrary Arguments

# # for example

# # -------------------------------------------------- arbitrary arguments


# def namesprint(*names):
#     print(names[0])
#     for i in names:
#         print(i)


# namesprint("shivraj", "sukraj", "ramanpreet")

# # if you need to pass value with it variable name or Arbitrary Keyword Arguments


# def argsname(**details):
#     print(details["name"])
#     print(details["address"])


# argsname(name="gurjit", address="amritsar")

# # ---------------------------------------- calling stack

# def first(a):
#     print("i am first", a)
#     return a + a

# def mid(a):
#     print("i am mid", a)
#     return a + a

# def last(a):
#     print("i am last", a)
#     return a + a

# result = first(mid(last(10)))

# print(result)

# # ---------------------------------------- lamda and use of lamda function

# x = lambda a: a + 10

# print(x(5))

# # use a function to make a another function


# def powerfun(n):
#     return lambda a: a * n


# squareof = powerfun(2)

# cubeof = powerfun(3)

# print(squareof(2))
# print(cubeof(2))

# # ----------------------------------------------------- recursion **

# # call same function inside that function

# #  a recursive function is a function that calls itself within its own code.
# # Recursion can be used to solve problems that can be broken down into smaller
# # subproblems of the same kind.

# # solve factorial using recursion


# def findfact(n):
#     if n <= 1:
#         return 1
#     else:
#         return n * findfact(n - 1)


# print("fact :", findfact(5))

# # view stack


# # ------------------------------------------------------ Global, Local and Nonlocal scopes

# # --------------------------GLOBAL
# # declare global variable
# message = "Hello"
# #  any variable outside any programmer defined scope is global scope

# def greet():
#     # declare local variable
#     print("Local", message)


# greet()
# print("Global", message)


# # -------------------------LOCAL
# def greet():
#     # local variable
#     message = "Hello"

#     print("Local", message)


# greet()

# # try to access message variable
# # outside greet() function
# # print(message) # give error


# # -------------------------NONLOCAL


# # outside function
# def outer():
#     message = "local"

#     # nested function
#     def inner():
#         # declare nonlocal variable
#         nonlocal message

#         message = "nonlocal"
#         print("inner:", message)

#     inner()
#     print("outer:", message)


# outer()
# print(message)

# # ------------------------------------------------------- use of global keyword

# # --> try to change global variable value in local scope
# c = 10


# def add():
#     # increment c by 2
#     c = c + 2

#     print(c)


# add()

# # re-declaration of global variable with "global" keyword


# def sub():
#     # use of global keyword
#     global c

#     # increment c by 2
#     c = c - 2

#     print(c)


# sub()

# # Output is 3
