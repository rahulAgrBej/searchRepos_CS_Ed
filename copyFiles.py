import os
from shutil import copyfile

def countToString(count):
    if count < 10:
        return '00' + str(count)
    elif count < 100:
        return '0' + str(count)
    
    return str(count)

fileNamesPath = 'testing.txt'
inDirPath = 'Data/Pruned_Files'
outDirPath = 'Data/PrunedLengthFiles'
f = open(fileNamesPath, 'r')
numFiles = int(f.readline().rstrip('\n'))

count = 0

for i in range(numFiles):
    currFileName = f.readline().rstrip('\n')
    newFileName = 'file' + countToString(count) + '.py'
    #srcFilePath = os.path.join(inDirPath, currFileName)
    srcFilePath = currFileName
    dstFilePath = os.path.join(outDirPath, newFileName)
    copyfile(srcFilePath, dstFilePath)
    count += 1

f.close()

print('Done copying files!')


