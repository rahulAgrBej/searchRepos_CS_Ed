import os
import hashlib

# creates a SHA-1 hash of a file
def hashFile(filePath):

    h = hashlib.sha1()

    f = open(filePath, 'rb')

    chunk = 0

    while chunk != b'':
        chunk = f.read(1024)
        h.update(chunk)
    
    return h.hexdigest()

# returns all duplicate file names in a folder
def findDuplicates(dirName):

    fileNames = os.listdir(dirName)
    checkDups = set()
    duplicates = []

    for fName in fileNames:
        currFilePath = os.path.join(dirName, fName)
        currFileHash = hashFile(currFilePath)

        if not (currFileHash in checkDups):
            checkDups.add(currFileHash)
        else:
            duplicates.append(fName)
    
    return duplicates

dataFolderPath = 'Data/Desired_Files'
dataDuplicates = findDuplicates(dataFolderPath)
print(dataDuplicates)
print(len(dataDuplicates))
            
