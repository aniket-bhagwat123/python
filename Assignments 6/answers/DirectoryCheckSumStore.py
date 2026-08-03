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

def FindDuplicate(dirName):
    ret = False
    ret = os.path.exists(dirName)
    if ret == False:
        print("Path does not exist")
        return
    
    if os.path.isdir(dirName) == False:
        print("This is not directory")
        return
    
    duplicate = {}
    unique = 0
    same = 0
    for fd, subf, fls in os.walk(dirName):
        for fl in fls:
            fl = os.path.join(fd, fl)
            checkSum = CalculateCheckSum(fl)
            print(f"{fl}: {checkSum}")
            if checkSum in duplicate:
                same += 1
                duplicate[checkSum].append(str(fl))
            else:
                unique += 1
                duplicate[checkSum] = [fl]
    
    print("Duplicate files: ", same)
    print("Unique files: ", unique)
    print("Duplicate files: ", duplicate)
            

def main():
    FindDuplicate("Test")

if __name__ == "__main__":
    main()