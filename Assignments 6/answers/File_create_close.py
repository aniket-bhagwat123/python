def main():
    try:
        fobj = open("Demo.txt", "w")
        print("File gets opened..")
        fobj.close()
    except FileNotFoundError:
        print("File is not found in current directory..")

if __name__ == "__main__":
    main()