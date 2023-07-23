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
