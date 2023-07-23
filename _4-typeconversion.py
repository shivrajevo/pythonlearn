# Implicit Type Conversion
# simple and automatic type conversion

print("example 1")
a = 20
b = 2.3
result = a + b

print(type(a), a)
print(type(b), b)
print(type(result), result)

print("example 2")

x = 10
y = 3
result = x / y

print(type(x), x)
print(type(y), y)
print(type(result), result)

# Explicit Type Conversion
# it prform by calling a funciton and forceful method gain errors

# m = 20 integer
m = 20
print(type(m), m)


m = m
print(type(m), m)

m = float(m)
print(type(m), m)

number = str("500")
print(type(number), number)

# output of progarm
'''
example 1
<class 'int'> 20
<class 'float'> 2.3
<class 'float'> 22.3

example 2
<class 'int'> 10
<class 'int'> 3
<class 'float'> 3.3333333333333335
<class 'int'> 20
<class 'int'> 20
<class 'float'> 20.0
<class 'str'> 500'''