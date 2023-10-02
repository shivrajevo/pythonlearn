# loops in python

# A loop is a programming function that repeats a statement or
# condition based on specified boundaries



# ----------------------------------- simple loop

for i in range(1,10):
    print(i)

# ----------------------------------- nested for loop

for i in range(1, 10):
    print("outer loop //////", i)
    for l in range(1, 10):
        print("inner loop", l)

# -------------------------------------  break pass continue
for i in range(1, 10):
    if i == 5:
        print("continue value", i)
        break
    print(i)
else:
    print("all done")


# -------------------------------------  while loop
a = 0
while a <= 10:
    a = a + 1
    if a == 5:
        continue
    print(a)
else:
    print("all done")
