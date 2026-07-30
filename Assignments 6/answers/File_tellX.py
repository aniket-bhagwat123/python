def main():
    try:
        fobj = open("Demo.txt", "r")
        print("File offset: ", fobj.tell()) # 0 offset
        print("File data: ", fobj.read(10))
        print("File offset: ", fobj.tell()) # 10 offset

        print("File data: ", fobj.read(10))
        print("File offset: ", fobj.tell())
        fobj.close()
    except FileNotFoundError:
        print("File is not found in current directory..")

if __name__ == "__main__":
    main()