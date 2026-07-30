#seek(end,start)

#0 = start
#1 = current
#2 = end
def main():
    try:
        fobj = open("Demo.txt", "r")
        print("File gets opned!")

        fobj.seek(10,0)

        data = fobj.read()

        print("File Data: ", data)

        fobj.close()
    except FileNotFoundError:
        print("File is not found in current directory..")

if __name__ == "__main__":
    main()