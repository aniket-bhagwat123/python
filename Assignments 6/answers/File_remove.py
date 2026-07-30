import os

def main():
    try:
        # fobj.remove() will not applicable
        os.remove("Demo.txt")
        print("Demo.txt file is deleted.")
        

    except FileNotFoundError:
        print("File is not found in current directory..")

if __name__ == "__main__":
    main()