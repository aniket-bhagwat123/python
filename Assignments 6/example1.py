# Q1) Count Lines in a File

# Write a program which accepts a file name from the user and counts how many lines are present in the file.
import sys

def GetFileName():
    FileName = sys.argv[1]
    return str(FileName)

def GetFilesLines():
    file = open(GetFileName(), "r")
    fileInLine = file.readlines()
    print(len(fileInLine))

def main():
    GetFilesLines()

if __name__ == "__main__":
    main()
