# "if-else statement" is a control structure used to make decisions based on certain conditions. It allows a program to execute different blocks of code depending on whether a specified condition is true or false.

# a = 10

# if a == 10:
#     if a == 15:
#         print("i am nested")
#     print("a is grater than b 10")
# elif a == 20:
#     print("a is less than b 20 ")
# elif a == 30:
#     print("a is less than b  30 ")
# elif a == 40:
#     print("a is less than b 40 ")
# elif a == 50:
#     print("a is less than b 50 ")
# elif a == 60:
#     print("a is less than b 60")
# else:
#     pass

# stored 
user   =  "iam"
passw = 1234


# filled

userin = input("enter user name :")
passwn = int(input("enter password :"))

if user == userin:
    if passw == passwn:
        print("you are login")
    else:
        print("user name ok but password is not")
else:
    print("password not match")