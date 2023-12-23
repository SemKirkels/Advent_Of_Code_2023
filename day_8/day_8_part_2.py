import math

df = open('input.txt').read().split('\n')

instructions = df[0]
instructions = instructions.replace("L", "0").replace("R", "1")
dest = dict()

for line in df[2:]:

    temp = [x.strip() for x in line.split("=")]
    source = temp[0]
    dest_list = [temp[1][1:-1].split(",")[0], temp[1][1:-1].split(",")[1]]
    dest[source] = dest_list

steps = 0
cycles = []
currents = [key for key in dest.keys() if key[-1] == "A"]

for c in currents:

    cycle = 0

    while c[-1] != "Z":

        cycle += 1

        for j in range(len(instructions)):

            if c[-1] != "Z":
                c = dest[c.strip()][int(instructions[j])]
            else:
                break

    cycles.append(cycle*len(instructions))

steps = math.lcm(*cycles)

print(steps)
