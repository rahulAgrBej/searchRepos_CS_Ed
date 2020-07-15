import pprint

mossFile = open('Data/MossOutput/moss0.txt', 'r')
mossLines = mossFile.readlines()
mossFile.close()

similarityThreshold = 90
clusters = {}
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

    if (percent0 >= similarityThreshold) and (percent1 >= similarityThreshold):
        if ((not (name0 in clusters)) and (not (name1 in clusters))):
            clusters[name0] = newClusterNum
            clusters[name1] = newClusterNum
            newClusterNum += 1
        elif ((not (name1 in clusters)) and (name0 in clusters)):
            clusters[name1] = clusters[name0]
        elif ((not (name0 in clusters)) and (name1 in clusters)):
            clusters[name0] = clusters[name1]

for fKey, fVal in clusters.items():
    if fVal == 0:
        print(fKey)
print()
pp.pprint(clusters)