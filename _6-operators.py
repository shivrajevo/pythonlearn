a = 10
b = 2

# Arithmetic Operators
# Assignment Operators
# Comparison Operators
# Logical Operators
# Identity operators
# Membership operators

print(" \n ARITHMETIC OPERATOR")
print("\n a = {} b = {} \n".format(a, b))
# addition
print("Sum: ", a + b)

# subtraction
print("Subtraction: ", a - b)

# multiplication
print("Multiplication: ", a * b)

# division
print("Division: ", a / b)

# floor division
print("Floor Division: ", a // b)

# modulo
print("Modulo: ", a % b)

# a to the power b
print("Power: ", a**b)


# Python Assignment Operators

print(" \n ASSIGNMENT OPERATOR")
x = 20
y = 10

print("\n a = {} b = {} \n".format(x, y))
# addition
y += x
print("Sum: ", y)

# subtraction
y -= x
print("Subtraction: ", y)

# multiplication
y *= x
print("Multiplication: ", y)

# division
y /= x
print("Division: ", y)

# floor division
y //= x
print("Floor Division: ", y)

# modulo
y %= x
print("Modulo: ", y)

# a to the power b
y **= x
print("Power: ", y)


# Python comparison Operators
print(" \n COMPARISON OPERATOR")

a = 5
b = 2

print("\n a = {} b = {} \n".format(a, b))
# equal to operator
print("a == b =", a == b)

# not equal to operator ! =
print("a != b =", a != b)

# greater than operator
print("a > b =", a > b)

# less than operator
print("a < b =", a < b)

# greater than or equal to operator > =
print("a >= b =", a >= b)

# less than or equal to operator  < =
print("a <= b =", a <= b)


#  Python Logical Operators
print(" \n LOGICAL OPERATOR")
# logical AND
print(True and True)  # True
print(True and False)  # False

# logical OR
print(True or False)  # True

# logical NOT
print(not True)  # False

# Identity operators in Python
print(" \n IDENTITY OPERATOR")

# "is" and  "is not"

x1 = 5
y1 = 5
x2 = "Hello"
y2 = "Hello"
x3 = [1, 2, 3]
y3 = [1, 2, 3]


print(x1 is not y1)  # prints False

print(x2 is y2)  # prints True

print(x3 is y3)  # prints False

# Membership operators in Python
print(" \n MEMBERSHIP OPERATOR")

# "in" and "not in"
x = "Hello world"
y = {1: "a", 2: "b"}

# check if 'H' is present in x string
print("H" in x)  # prints True

# check if 'hello' is present in x string
print("hello" not in x)  # prints True

# check if '1' key is present in y
print(1 in y)  # prints True

# check if 'a' key is present in y
print("a" in y)  # prints False
