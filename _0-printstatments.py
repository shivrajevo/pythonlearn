# simple hello world program
print("hello world")

# use of seprator
print("shivraj", "ranjit", sep="-")

# print multile string using *
print("shivraj " * 5)

# concatinate
print("shivraj " + "stark")

# format string
print("your name is {} and number is {}".format("shivraj", 55005500))

# console input
name = input("enter your name ")
print("hello " + name)

# input with the use of type casting
number = int(input("enter your number"))
print("your number is ", number)

# inline statement of above input
print(input("enter your name : "), int(input("enter your number :")))

# output of program
'''
hello world
shivraj-ranjit
shivraj shivraj shivraj shivraj shivraj
shivraj stark
your name is shivraj and number is 55005500
enter your name shivraj stark
hello shivraj stark
enter your number45121
your number is  45121
enter your name : shivraj
enter your number :452485
shivraj 452485'''
