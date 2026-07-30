import os

def main():
    for Foldername, subfolder, filename in os.walk("Marvellous"):
        print("Folder name: ", Foldername)
        for subf in subfolder:
            print("Subfolder names: ", subf)

if __name__ == "__main__":
    main()