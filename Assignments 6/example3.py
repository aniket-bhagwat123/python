# Q3) Display File Line by Line

# Write a program which accepts a file name from the user and displays the contents of the file line by line on the
# screen.

import sys

def GetFileName():
    name = sys.argv[1]
    return name 


def FileLineByLine():
    file = open(GetFileName(), "r")

    read = file.readlines()

    for i in read:
        print(i, end="")


def main():
    FileLineByLine()

if __name__ == "__main__":
    main()