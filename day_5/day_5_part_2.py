import math

df = open('input.txt').read().split('\n')

seeds = [int(x) for x in df[0].split(':')[1].strip().split(' ')]
seed_to_soil = []
soil_to_fertilizer = []
fertilizer_to_water = []
water_to_light = []
light_to_temperature = []
temperature_to_humidity = []
humidity_to_location = []

maps = [seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location]

i = 0

for line in df[2:]:
    if line == '':
        i += 1
    elif ':' in line:
        continue
    else:
        maps[i].append([int(x) for x in line.split(' ')])

newSeeds = []

for i in range(0, len(seeds), 2):

    for j in range(seeds[i], seeds[i] + seeds[i+1]):

        if j not in newSeeds:
            newSeeds.append(j)

def mapToNext(value, list):

    for item in list:

        if item[1] <= value < item[1] + item[2]:
            return item[0] + (value-item[1])    

    return value

minLoc = math.inf

for value in newSeeds:

    next = value

    for i in range(len(maps)):
        next = mapToNext(next, maps[i])

    if next < minLoc:
        minLoc = next

print(minLoc)
