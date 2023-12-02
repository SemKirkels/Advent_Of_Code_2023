fd = open("input.txt").read().split('\n')
count = 0
maxCubes = {'red': 12, 'green':13, 'blue': 14}

for line in fd:
    temp = line.split(':')
    gameID = temp[0].split(' ')[1]

    isPossible = True

    for sets in temp[1].split(';'):
        for cube in sets.split(','):
            for key in maxCubes.keys():
                if key in cube:
                    if maxCubes[key] < int(cube.split(' ')[1].strip()):
                        isPossible = False
    if isPossible:
        count += int(gameID)
print(count)