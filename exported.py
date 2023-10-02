# the above function is use to call as default statement
def main():
    pass

# we create for basic calculation function for export
def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


def div(x, y):
    return x / y

pi = 3.14
# if __name__ == "__main__" that means the current file is running
if __name__ == "__main__":
    # we also use pass insted of main() function
    main()
    print("exported file runned")
