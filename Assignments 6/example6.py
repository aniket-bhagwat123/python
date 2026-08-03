# Q1) Check File Exists in Current Directory

# Problem Statement:
# Write a program which accepts a file name from the user and checks whether that file exists in the current
# directory or not.

from pathlib import Path
import sys

filename = str(input("Enter a file name"))

def CheckFileExits():
    isfound = Path.is_file(filename)

    if isfound:
        print("File is exits on current directory")
    else:
        print("File does not exits on current directory")


def main():
    CheckFileExits()


if __name__ == "__main__":
    main()
