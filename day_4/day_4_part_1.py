df = open('input.txt')
points = []

for line in df:

    row = line.split(":")[1]
    winRow = [int(x.strip()) if x != '' else None for x in row.split('|')[0].split(' ')]
    myRow = [int(x.strip()) if x != '' else None for x in row.split('|')[1].split(' ')]

    temp = 0

    for num in myRow:

        if num is not None and num in winRow:
            if temp == 0:
                temp += 1
            else:
                temp *= 2
    points.append(temp)
    
print(sum(points))