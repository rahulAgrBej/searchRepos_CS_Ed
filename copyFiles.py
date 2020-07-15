import os
from shutil import copyfile

fileNamesPath = 'Data/prunedFiles.txt'
inDirPath = 'Data/Desired_Files'
outDirPath = 'Data/Pruned_Files/'
f = open(fileNamesPath, 'r')
numFiles = int(f.readline().rstrip('\n'))

for i in range(numFiles):
    currFileName = f.readline().rstrip('\n')
    srcFilePath = os.path.join(inDirPath, currFileName)
    dstFilePath = os.path.join(outDirPath, currFileName)
    copyfile(srcFilePath, dstFilePath)

f.close()

print('Done copying files!')
