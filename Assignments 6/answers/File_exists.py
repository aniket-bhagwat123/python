import os

def main():
    ret = os.path.exists("Demo.txt")

    if ret == True:
        print("File is exist.")
    else:
        print("File is not exists.")

if __name__ == "__main__":
    main()