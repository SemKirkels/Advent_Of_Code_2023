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
        df.insert(i+1+appendedRows, "".join(["e" for _ in range(len(map[i]))]))
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

            row.insert(i+appendedCol, "empty")
        appendedCol += 1

pMap = impMap.copy()
galaxy = dict()
nGalaxy = 1

for i in range(len(pMap)):

    for j in range(len(pMap[i])):

        if pMap[i][j] == "#":
            galaxy[nGalaxy] = [i,j]
            nGalaxy += 1

paths = []
expand = 1000000 - 2

for i in range(len(galaxy.keys())):

    for j in range(i + 1, len(galaxy.keys())):

        fstPoint = galaxy[list(galaxy.keys())[i]]
        sndPoint = galaxy[list(galaxy.keys())[j]]
        nEmpRow = 0
        nEmpCol = 0

        for x in range(abs(fstPoint[0] - sndPoint[0])):
            if pMap[fstPoint[0]+x][fstPoint[1]] == "e":
                nEmpRow += 1

        if sndPoint[1] >= fstPoint[1]:
            for y in range(fstPoint[1]+1, sndPoint[1]+1):

                if pMap[sndPoint[0]][y] == "empty":
                    nEmpCol += 1
        else:
            for y in range(sndPoint[1]+1, fstPoint[1]+1):

                if pMap[sndPoint[0]][y] == "empty":
                    nEmpCol += 1

        paths.append(abs(fstPoint[0] - sndPoint[0]) + abs(fstPoint[1] - sndPoint[1]) + (nEmpRow + nEmpCol) * expand)

print(sum(paths))