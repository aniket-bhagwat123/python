# Q2) Display File Contents
# Problem Statement:
# Write a program which accepts a file name from the user, opens that file, and displays the entire contents on the
# console.

import sys

def GetFileName():
    return sys.argv[1]

def PrintAllContent():
    file = open(GetFileName(), "r")

    write = file.read()
    print(write)

    file.close()

def main():
    PrintAllContent()

if __name__ == "__main__":
    main()
