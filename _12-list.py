# # In Python, a list is a built-in data structure used to store a collection of items.
# # These items can be of any data type, including numbers, strings, other lists, or even more complex objects.
# # Lists are ordered and mutable, which means you can modify their content after they are created.


# # ---------------------------------------------- (syntax to create list on python )

# list1 = ["cat", 2, 3.14, True]
# #  index   0    1    2    3
# #  index  -4   -3   -2   -1

# # for accessing : "cat"
# # listname[index no]

# print(list1[0])

# # of need to access the last element  you can access by
# print(list1[-1])

# print("to find the length of list", len(list1))
# # len function count the item of a list

# # delete a element on list

# del list1[0]

# print(list1)

# # --------------------------------------------------- (Slicing a list)
# # List slicing in Python

# brands = ["mi", "nokia", "samsung", "apple", "redmi", "realme"]

# # items from index 1 to index 3  (n-1)
# print("\n", brands[1:4])

# # from index 2 to end
# print(brands[2:])

# # from index 0 to 1 (n-1)
# print(brands[:2])

# # methods of list in python


# print("\n ------------------------(use of methods)------------------------- \n")
# print("ORIGNAL LIST:", brands)

# # append()
# # extend()
# # insert()
# # remove()
# # pop()
# # clear()
# # index()
# # count()
# # sort()
# # reverse()
# # copy()

# # let explore them one by one

# # -----------------------------------------------------------------------------
# # append()	add an item to the end of the list
# brands.append("HP")

# print("\nusing append:", brands)
# # -----------------------------------------------------------------------------
# # extend()	add all the items of an iterable to the end of the list
# list2 = ["brand1", "brand2"]

# brands.extend(list2)
# print("using extend:", brands)
# # -----------------------------------------------------------------------------
# # insert()	inserts an item at the specified index

# brands.insert(2, "poco")
# print("using insert:", brands)

# # -----------------------------------------------------------------------------
# # remove()	removes item present at the given index
# # ! cannot remove element using index no

# brands.remove("mi")
# print("using remove:", brands)
# # -----------------------------------------------------------------------------
# # pop()	    returns and removes item present at the given index

# print("\nbefore  :", brands)

# brands.pop(-1)
# print("using pop:", brands)

# brands.pop(-1)
# print("using pop:", brands)

# brands.pop(0)
# print("using pop:", brands)

# # -----------------------------------------------------------------------------
# # index()	returns the index of the first matched item
# find = "nokia"

# i = brands.index(find)

# print(f"\nindex of {find} is", i)

# # -----------------------------------------------------------------------------
# # count()	returns the count of the specified item in the list

# numbers = [1, 2, 5, 2, 6, 4, 2, 8, 4, 3, 2]

# numb = 2

# print(f"count of {numb} in list is", numbers.count(numb))

# # -----------------------------------------------------------------------------
# # sort()	sort the list in ascending/descending order

# print("\nbefore sorting", numbers)
# numbers.sort()
# print("after sorting", numbers)
# numbers.sort(reverse=True)
# print("reverse order", numbers)

# # -----------------------------------------------------------------------------
# # reverse()	reverses the item of the list

# numbers.reverse()
# print("\nafter reverse method :", numbers)

# # -----------------------------------------------------------------------------
# # copy()	returns the shallow copy of the list

# numbers2 = numbers.copy()

# print("\nnumbers  : ", numbers)
# print("numbers2 : ", numbers2)

# # -----------------------------------------------------------------------------

# print("\n before use of clear", brands)
# brands.clear()
# print("after use of clear : ", brands)


# Program to multiply two matrices using nested loops

# 3x3 matrix
X = [[12, 7, 3], [4, 5, 6], [7, 8, 9]]
# 3x4 matrix
Y = [[5, 8, 1, 2], [6, 7, 3, 0], [4, 5, 9, 1]]
# result is 3x4
result = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

# iterate through rows of X
for i in range(len(X)):
    # iterate through columns of Y
    for j in range(len(Y[0])):
        # iterate through rows of Y
        for k in range(len(Y)):
            result[i][j] += X[i][k] * Y[k][j]

for r in result:
    print(r)
