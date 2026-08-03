# Q3) Copy File Contents into a New File (Command Line)
# Problem Statement:
# Write a program which accepts an existing file name through command line arguments, creates a new file
# named Demo.txt, and copies all contents from the given file into Demo.txt

import sys
import shutil

def GetFileName():
    return sys.argv[1]

def CopyAllToNewFile():
    newfile = "new_file.txt"

    shutil.copy(GetFileName(), newfile)

    print(f"Copy contents of {GetFileName()} into {newfile}.")
    

def main():
    CopyAllToNewFile()

if __name__ == "__main__":
    main()
