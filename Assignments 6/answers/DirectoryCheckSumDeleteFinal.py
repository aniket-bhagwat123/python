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
    for fd, subf, fls in os.walk(dirName):
        for fl in fls:
            fl = os.path.join(fd, fl)
            checkSum = CalculateCheckSum(fl)
            # print(f"{fl}: {checkSum}")

            if checkSum in duplicate:
                duplicate[checkSum].append(str(fl))
            else:
                duplicate[checkSum] = [fl]
    
    return duplicate

def DeleteDuplicate(dirName):
    myDict = FindDuplicate(dirName)
    
    result = list(filter(lambda x: len(x) > 1, myDict.values()))
    count = 0
    totalDeleted = 0
    for val in result:
        for v in val:
            count += 1
            if count > 1:
                os.remove(v)
                totalDeleted += 1
        count = 0

    print("Total deleted files: ", totalDeleted)

    
def main():
    data = DeleteDuplicate("Test")
    

if __name__ == "__main__":
    main()