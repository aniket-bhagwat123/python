import sys
import os
import hashlib

def CalculateCheckSum(fileName):
    fobj = open(fileName, "rb")
    hobj = hashlib.md5()
    buffer = fobj.read(1024)
    while(len(buffer) > 0):
        hobj.update(buffer)
        buffer = fobj.read(1024)

    fobj.close()

    return hobj.hexdigest()


def main():
    ret = CalculateCheckSum("Demo.txt")
    print("Checksum of file: ", ret)

if __name__ == "__main__":
    main()