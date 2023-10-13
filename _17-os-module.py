# PYTHON OS MODULE
import os
import os.path


# # insert command directly on terminal
# # for example we insert cls to clear the terminal
# os.system("cls")

# # to create the folder
# os.mkdir()

# # to change the filename (in same dir)
# os.rename("oldname.txt", "newname.txt")

# # we also use it for copy the file from one dir to another
# os.rename("C:\\files\example.txt", "C:\\backup\example.txt")

# # to delete a file
# os.remove("filename.txt")

# # to change the directory at runtime
# os.chdir(os.getcwd() + "\..")

# # returns the current working directory
# cwd = os.getcwd()

# # to list the all files and directory in python
# print(cwd, os.listdir())


# # making a function that list all the contents in directory
def list_all():
    flag = 0
    print("LIST ALL DIRECTORY ")
    for i in os.listdir():
        print(f"{flag} > ", i)
        flag += 1


# # making a function that list all the folder in a directory
def list_folder():
    flag = 0
    print("FOLDERS IN DIRECTORY")
    for i in os.listdir():
        if os.path.isdir(i):
            print(f"{flag} > ", i)
            flag += 1


# # making a function that list only files only
def list_fileonly():
    flag = 0
    print("FILES IN DIRECTORY")
    for i in os.listdir():
        if os.path.isdir(i):
            continue
        else:
            print(f"{flag} > ", i)
            flag += 1


# #  with os.walk we get all roots ,dir in roots in list , and files for
# #  use this we make a function
def get_alldirs():
    flag = 0
    for root, dirs, files in os.walk(".", topdown=True):
        flag += 1
        print(f"{flag} ", root)
        # print(dirs)
        # print("-----------------")
        # print(files)
