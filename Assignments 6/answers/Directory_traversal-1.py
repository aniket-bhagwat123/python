import os

def main():
    for Foldername, subfolder, filename in os.walk("Marvellous"):
        print(Foldername)

if __name__ == "__main__":
    main()