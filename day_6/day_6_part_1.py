import re

df = open('input.txt').read().split('\n')

times = [int(x) for x in re.findall(r'\d+', df[0])]
distances = [int(x) for x in re.findall(r'\d+', df[1])]
numberOfWays = 1

for i in range(len(times)):

    nWays = 0

    for j in range(times[i]):

        if (times[i] - j) * j > distances[i]:
            nWays += 1

    numberOfWays *= nWays

print(numberOfWays) 