fd = open("input.txt").read().split('\n')
output = []

for line in fd:
    temp = line.split(':')
    minCubes = {'red': 1, 'green': 1, 'blue': 1}
    
    for sets in temp[1].split(';'):
        for cube in sets.split(','):
            for key in minCubes.keys():
                if key in cube:
                    if minCubes[key] < int(cube.split(' ')[1].strip()):
                        minCubes[key] = int(cube.split(' ')[1].strip())
    output.append(minCubes['red'] * minCubes['green'] * minCubes['blue'])
print(sum(output))