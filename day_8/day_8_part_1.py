import math

df = open('input.txt').read().split('\n')

instructions = df[0]
instructions = instructions.replace("L", "0").replace("R", "1")
destinations = dict()

for line in df[2:]:

    temp = [x.strip() for x in line.split("=")]
    source = temp[0]
    dest = [temp[1][1:-1].split(",")[0], temp[1][1:-1].split(",")[1]]
    destinations[source] = dest

steps = 0
notFound = True
curr = "AAA"

while notFound:

    for i in range(len(instructions)):

        where = int(instructions[i])
        curr = destinations[curr][where].strip()
        steps += 1

        if curr == "ZZZ":

            notFound = False
            print(steps)
            break
