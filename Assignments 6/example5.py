# Write a program which accepts a file name and a word from the user and checks whether that word is present in
# the file or not.

import sys

word = input("Enter A word").lower()

def GetFileName():
    return sys.argv[1]

def FindWordIntoFile():
    try:
        file = open(GetFileName(), "r")

        read_file = file.read()
        split = read_file.lower().split()

        find = list(filter(lambda x: x == word, split))

        if len(find) > 0:
            print(f"The word '{word}' is found in {GetFileName()}")
        else:
            print(f"The word '{word}' not found in {GetFileName()}")
    except FileNotFoundError:
        print("File is not found")
    except Exception as e:
        print(e)

def main():
    FindWordIntoFile()

if __name__ == "__main__":
    main()