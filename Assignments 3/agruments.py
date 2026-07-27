# Positional Arguments
# Keyword Arguments
# Default Arguments
# Variable Number of Arguments



# 1. Positional Arguments

def pos(f1, f2):
    total = f1 + f2
    print(f"Positional Arguments: {total}")


pos(10, 10)



# 2. Keyword Arguments

def keys(f1, f2):
    subtr = f1 - f2
    print(f"Keyword Arguments: {subtr}")


keys(10, 5)



# 3. Default Arguments

def default(f1, f2 = 5):
    add = f1 + f2
    print(f"Default Arguments: {add}")


default(2)


# 3. Variable Number of Arguments

def notfixed(*args):
    print(args)


notfixed(10, 20, 50)

