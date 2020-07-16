
f = open('Data/similarLengthFiles.txt', 'r')
fLines = f.readlines()
f.close()

similarityThresh = 90
relevantFiles = set()

for line in fLines:
    line = line.rstrip('\n')
    files = line.split('\t')
    
    fileData0 = files[0].split(' ')
    fileName0 = fileData0[0]
    filePercent0 = int(fileData0[1][1:-2])

    fileData1 = files[0].split(' ')
    fileName1 = fileData1[0]
    filePercent1 = int(fileData1[1][1:-2])

    # first check if either files are above the similarity threshold
    if (filePercent0 > similarityThresh) or (filePercent1 > similarityThresh):
        
        # save the file name with the lower percentage
        if filePercent0 > filePercent1:
            relevantFiles.add(fileName1)
        else:
            relevantFiles.add(fileName0)
    else:
        # save both the file names
        relevantFiles.add(fileName1)
        relevantFiles.add(fileName0)

print(len(relevantFiles))
for name in relevantFiles:
    print(name)
