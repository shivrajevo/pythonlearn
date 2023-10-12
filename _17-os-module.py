# PYTHON OS MODULE

import os
import os.path


# insert command directly on terminal
os.system("cls")

# to create the folder
# os.mkdir()

cwd = os.getcwd()
# returns the current working directory

# to list the all files and directory in python
print(cwd, os.listdir())


# making a function that list all the contents in directory
def list_all():
    flag = 0
    print("LIST ALL DIRECTORY ")
    for i in os.listdir():
        print(f"{flag} > ", i)
        flag += 1



# making a function that list all the folder in a directory
def list_folder():
    flag = 0
    print("FOLDERS IN DIRECTORY")
    for i in os.listdir():
        if os.path.isdir(i):
            print(f"{flag} > ", i)
            flag += 1


# making a function that list only files only
def list_fileonly():
    flag = 0
    print("FILES IN DIRECTORY")
    for i in os.listdir():
        if os.path.isdir(i):
            continue
        else:
            print(f"{flag} > ", i)
            flag += 1
