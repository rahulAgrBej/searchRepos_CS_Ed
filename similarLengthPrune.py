
f = open('Data/similarLengthFiles.txt', 'r')
fLines = f.readlines()
f.close()

similarityThresh = 90
relevantFiles = set()
blackList = set()

for line in fLines:
    line = line.rstrip('\n')
    files = line.split('\t')
    
    fileData0 = files[0].split(' ')
    fileName0 = fileData0[0]
    filePercent0 = int(fileData0[1][1:-2])

    fileData1 = files[1].split(' ')
    fileName1 = fileData1[0]
    filePercent1 = int(fileData1[1][1:-2])

    print(f'{fileName0} {filePercent0} {fileName1} {filePercent1}')

    # check if either file is in the black list first
    if fileName0 in blackList:
        relevantFiles.add(fileName1)
    elif fileName1 in blackList:
        relevantFiles.add(fileName0)
    else:
        # first check if either files are above the similarity threshold
        if (filePercent0 > similarityThresh) or (filePercent1 > similarityThresh):
            
            
            
            # save the file name with the lower percentage
            if filePercent0 > filePercent1:
                relevantFiles.add(fileName1)

                # blacklist the other file
                blackList.add(fileName0)
                print(f'{fileName1} added')
            else:
                relevantFiles.add(fileName0)
                print(f'{fileName0} added')
                # black list the other file
                blackList.add(fileName1)

        else:
            # save both the file names
            relevantFiles.add(fileName1)
            relevantFiles.add(fileName0)
            print(f'both {fileName0} {fileName1}')

print(len(relevantFiles))

fOut = open('testing.txt', 'w')
for name in relevantFiles:
    fOut.write(name)
    fOut.write('\n')

fOut.close()