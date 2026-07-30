# Q4) Copy File Contents into Another File

# Write a program which accepts two file names from the user.
    # • First file is an existing file
    # • Second file is a new file

import sys
import shutil

def getTwoFilesName():
    return sys.argv[1], sys.argv[2] 

def CopyFileForAnother():
    file , file2 = getTwoFilesName()

    try:
        shutil.copy(file, file2)
        print(f"Contents of {file} copied into {file2}.")
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print("Error", e)
    

def main():
    CopyFileForAnother()


if __name__ == "__main__":
    main()
    