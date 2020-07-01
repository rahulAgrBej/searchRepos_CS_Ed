import os
from dataPruning import hashFile

# path to duplicate test folder
dupFolderPath = 'tests/testingDup'

fileNames = os.listdir(dupFolderPath)

checkDups = {}

for i in range(len(fileNames)):
    currFileName = fileNames[i]
    currPath = os.path.join(dupFolderPath, currFileName)
    currFileHash = hashFile(currPath)
    
    if not (currFileHash in checkDups):
        checkDups[currFileHash] = []
    
    checkDups[currFileHash].append(currFileName)

print(checkDups)