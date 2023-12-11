import re

df = open('input.txt').read().split('\n')

times = int("".join([x for x in re.findall(r'\d+', df[0])]))
distances = int("".join([x for x in re.findall(r'\d+', df[1])]))
numberOfWays = 0

for i in range(times):

    if (times - i) * i > distances:
        numberOfWays += 1

print(numberOfWays)