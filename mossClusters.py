import pprint

mossFile = open('Data/MossOutput/moss0.txt', 'r')
mossLines = mossFile.readlines()
mossFile.close()

similarityThreshold = 90
clustersByFname = {}
newClusterNum = 0

pp = pprint.PrettyPrinter(indent=2)

for line in mossLines:
    tabSplit = line.split('\t')
    file0 = tabSplit[0].split(' ')
    file1 = tabSplit[1].split(' ')

    name0 = file0[0]
    name1 = file1[0]

    percent0 = int(file0[1][1:-2])
    percent1 = int(file1[1][1:-2])

    if (percent0 >= similarityThreshold) or (percent1 >= similarityThreshold):
        if ((not (name0 in clustersByFname)) and (not (name1 in clustersByFname))):
            clustersByFname[name0] = newClusterNum
            clustersByFname[name1] = newClusterNum
            newClusterNum += 1
        elif ((not (name1 in clustersByFname)) and (name0 in clustersByFname)):
            clustersByFname[name1] = clustersByFname[name0]
        elif ((not (name0 in clustersByFname)) and (name1 in clustersByFname)):
            clustersByFname[name0] = clustersByFname[name1]

clusters = {}

for fKey, fVal in clustersByFname.items():
    if not (fVal in clusters):
        clusters[fVal] = []
    clusters[fVal].append(fKey)

for clusterKey in clusters.keys():
    filePath = 'Data/MossOutput/MossClusters/cluster' + str(clusterKey)
    fOut = open(filePath, 'w')
    for fFound in clusters[clusterKey]:
        fOut.write(fFound)
        fOut.write('\n')
    fOut.close()