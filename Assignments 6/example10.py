# Q5) Frequency of a String in File
# Problem Statement:
# Write a program which accepts a file name and one string from the user and returns the frequency (count of
# occurrences) of that string in the file.

# import sys

file = str(input("Enter a file name"))
word = str(input("Enter a word"))


def Check_Occurrences():
    try:
        get = open(file, "r")
        readfile = get.read() 

        count = readfile.count(word)
        print(count)
    except Exception as e:
        print(e)


def main():
    Check_Occurrences()

if __name__ == "__main__":
    main()
