# Statement, Indentation and Comment in Python

"""A Python statement is an instruction that the Python interpreter can execute.
 There are different types of statements in Python language as Assignment statements,
   Conditional statements, Looping statements, etc. """

# for example
print("it is also a statement ")

for i in range(1, 10 + 1):
    print(i)


# differnt types of comments in python

# comment by #

# comment by """ """
""" python
    statement
    loop"""

# Docstring :-
# is like a documentation about the function
def add(a, b):
    """a function to add two numbers

    Args:
        a (int): value 1
        b (int): value 2
    """
    return a + b


print(add.__doc__)
# output
'''a function to add two numbers

    Args:
        a (int): value 1
        b (int): value 2'''

# tostring()
# convert that comment lines into string and remove holder of other functions 
# over all structure of a android program is very safe and secure of
# for internal bleading afterall 