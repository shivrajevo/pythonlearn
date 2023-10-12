# PYTHON FILE HEANDLING 

# r: open an existing file for a read operation.
# w: open an existing file for a write operation. If the file already contains some data then it will be overridden but if the file is not present then it creates the file as well.
# a: open an existing file for append operation. It won’t override existing data.
# x: With this mode, you can create a file and then write to it dynamically using methods that you will learn in just a few moments.
# r+: To read and write data into the file. The previous data in the file will be overridden.
# w+: To write and read data. It will override existing data.
# a+: To append and read data from the file. It won’t override existing data.



print("--------------(CREATE THE FILE)--------------------------")

filec = open("simple2.txt", "x")

filec.close()

print("--------------(READING THE FILE)--------------------------")

# open a file
file1 = open("simple.txt", "r")

# read the file
data = file1.read()
print(data)

file1.close()


print("------------------(WRITING IN FILE)---------------------------")

print("read file in write mode")
file2 = open("simple.txt", "w")

# print("read file in append mode")
# file2 = open("simple.txt", "a")

file2.write("Programming is Fun.")

# file2.write("Programiz for beginners")

file2.close()

file2 = open("simple.txt", "r")

print(file2.read())

file2.close()

print("------------------(READ FILE LINEWISE)---------------------------")

file3 = open("simple1.txt", "r")

print(file3.readline())
print(file3.readline())
print(file3.readline())

file3.close()

print("------------------(REMOVE FILE)---------------------------")

import os

os.remove("simple1.txt")
