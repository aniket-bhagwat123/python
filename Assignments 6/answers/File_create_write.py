def main():
    try:
        fobj = open("Demo.txt", "w")
        print("File gets opened..")
        fobj.write("This is Demo file..Jay Ganesh!!")
        fobj.close()
    except FileNotFoundError:
        print("File is not found in current directory..")

if __name__ == "__main__":
    main()