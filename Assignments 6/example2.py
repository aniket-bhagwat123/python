# Q2) Count Words in a File

# Write a program which accepts a file name from the user and counts the total number of words in that file.
import sys

def GetFileName():
    filename = sys.argv[1]
    return filename

def CountWords():
    file = open(GetFileName(), "r")
    read = file.read().split()
    total = 0

    for i in read:
        total += 1

    print(f"Total number of words : {total}") 
    print(f"Total number of words : {len(read)}") 

def main():
    CountWords()

if __name__ == "__main__":
    main()
