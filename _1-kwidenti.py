# Keywords and Identifires

# keywords
# Python Keywords are some predefined and reserved words in python that have special 
# meanings. Keywords are used to define the syntax of the coding. The keyword cannot be 
# used as an identifier, function, or variable name. All the keywords in python are 
# written in lowercase except True and False.

# to get a list of all identifiers
import keyword

print(keyword.kwlist)

print("total number keyword in this version is ", keyword.kwlist.__len__())

# Identifier is a user-defined name given to a variable, function, class, module, etc.
#  The identifier is a combination of character digits and an underscore. They are case-s
#  ensitive i.e., "num" and "Num" and "NUM" are three different identifiers in python. 
#  It is a good programming practice to give meaningful names to identifiers to make the 
#  code understandable.

# Valid identifiers:

# var1
# _var1
# _1_var
# var_1
# Invalid Identifiers

# !var1
# 1var
# 1_var
# var#1
# var 1


# output of program
# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 
# 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 
# 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
# total number keyword in this version is  35
