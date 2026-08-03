# Q4) Compare Two Files (Command Line)

# Problem Statement:
# Write a program which accepts two file names through command line arguments and compares the contents of
# both files.
# • If both files contain the same contents, display Success
# • Otherwise display Failure

import sys
import hashlib

def FileNames():
    return sys.argv[1], sys.argv[2]

def checkSum(file):
    currentfile = hashlib.md5()

    with open(file, "rb") as a:
        buffer = a.read()
        currentfile.update(buffer)

    return currentfile.hexdigest()


def main():
    file1, file2 = FileNames()
    checkSum1 = checkSum(file1)
    checkSum2 = checkSum(file2)

    if checkSum1 == checkSum2:
        print("Success")
    else:
        print("Failure")


if __name__ == "__main__":
    main()
