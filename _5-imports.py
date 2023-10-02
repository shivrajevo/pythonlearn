# A Python module is a file containing Python definitions and statements.
# A module can define functions, classes, and variables.
# A module can also include runnable code.
# Grouping related code into a module makes the code easier to understand and use.
# It also makes the code logically organized.

# making own modules in python

import exported


# import a local module
import math
# import os

# os.system("cls")

# print(exported.add(10, 20))

print(math.pi)

# print(os.getcwd())

# # output
# '''30
# 3.141592653589793
# C:\Users\directory name '''


import exported as ex

var = ex.add(10, 20)

print(exported.pi)
