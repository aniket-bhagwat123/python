import os

def main():

    if os.path.exists("Demo.txt"):
        print("File is exist.")
    else:
        print("File is not exists.")

if __name__ == "__main__":
    main()