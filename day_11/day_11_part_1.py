from copy import deepcopy

df = open('input.txt').read().split('\n')

map = [[c for c in line.strip()] for line in df]
appendedRows = 0

for i in range(len(map)):

    noGalaxy = True
        
    for j in range(len(map[i])):

        if map[i][j] == "#":
            noGalaxy = False
            break

    if noGalaxy:
        df.insert(i+1+appendedRows, "".join(["." for _ in range(len(map[i]))]))
        appendedRows += 1

impMap = [[c for c in line.strip()] for line in df]
cpImpMap = deepcopy(impMap)
appendedCol = 1

for i in range(len(cpImpMap[0])):

    noGalaxy = True

    for j in range(len(cpImpMap)):

        if cpImpMap[j][i] == "#":
            noGalaxy = False
            break

    if noGalaxy:

        for row in impMap:

            row.insert(i+appendedCol, ".")

        appendedCol += 1

pMap = impMap.copy()

galaxy = dict()
nGalaxies = 1

for i in range(len(pMap)):

    for j in range(len(pMap[i])):

        if pMap[i][j] == "#":
            galaxy[nGalaxies] = [i,j]
            nGalaxies += 1

paths = []

for i in range(len(galaxy.keys())):

    for j in range(i + 1, len(galaxy.keys())):

        fstPoint = galaxy[list(galaxy.keys())[i]]
        sndPoint = galaxy[list(galaxy.keys())[j]]
        paths.append(abs(fstPoint[0] - sndPoint[0]) + abs(fstPoint[1] - sndPoint[1]))

print(sum(paths))