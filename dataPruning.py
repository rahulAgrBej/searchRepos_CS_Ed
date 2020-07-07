import os
import hashlib
import re

# builds a regexOR expression
def buildRegexOR(exprList):

    regexOR = ''

    for i in range(len(exprList)):
        regexOR += exprList[i]

        if (i < (len(exprList) - 1)):
            regexOR += '|'

    return regexOR

# creates a SHA-1 hash of a file
def hashFile(filePath):

    h = hashlib.sha1()

    f = open(filePath, 'rb')

    chunk = 0

    while chunk != b'':
        chunk = f.read(1024)
        h.update(chunk)
    
    f.close()
    
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

# will check if a file has the importStatements you are looking for
def checkImports(filePath, importStatements):

    f = open(filePath, 'r')
    fContents = f.read()
    f.close()

    regexStr = buildRegexOR(importStatements)

    results = re.findall(regexStr, fContents)

    if len(results) > 0:
        return True

    return False


def importBasedPrune(dirName, importStatements):

    fileNames = os.listdir(dirName)
    duplicates = findDuplicates(dirName)\

    fileNames = sorted(fileNames)
    duplicates = sorted(duplicates)
    
    dupIdx = 0

    relevantFileNames = []
    
    for idx in range(len(fileNames)):
        
        currFileName = fileNames[idx]
        currDupName = duplicates[dupIdx]
        
        if (currFileName != currDupName):
            filePath = os.path.join(dirName, currFileName)
            hasImports = checkImports(filePath, importStatements)
            
            if hasImports:
                relevantFileNames.append(currFileName)
        elif (currFileName == currDupName):
            dupIdx += 1
        
        if (dupIdx == len(duplicates)):
            break
    
    
    return relevantFileNames



soupImports = [
    'import bs4',
    'from bs4 import BeautifulSoup',
    'import BeautifulSoup',
    'from BeautifulSoup import BeautifulSoup'
    ]

dataFolder = 'Data/Desired_Files'
relevantFileNames = importBasedPrune(dataFolder, soupImports)

fOut = open('Data/prunedFiles.txt', 'w')
fOut.write(str(len(relevantFileNames)) + '\n')

for relFile in relevantFileNames:
    fOut.write(relFile + '\n')

fOut.close()