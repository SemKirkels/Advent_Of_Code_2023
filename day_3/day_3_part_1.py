fd = open("input.txt")

dataMatrix = [line for line in fd]
chars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '/', '?', '<', '>']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
temp = [-1]

# matrix
# (x-1, y-1)(x-1, y)(x-1, y+1)
# (x, y-1)  (x, y)  (x, y+1)
# (x+1, y-1)(x+1, y)(x+1, y+1)

def readNumbers(list, pos):
    index = pos
    num = []

    if list[index - 1] in numbers:
        index -= 1
    
    if index - 1 >= 0:
        if list[index - 1] in numbers:
            index -= 1 
    
    for pos in range(3):
        if list[index] not in numbers:
            break
        num.append(list[index])
        index += 1
        
    return int("".join(num))

for x in range(1,len(dataMatrix) - 1):
    for y in range(1, len(dataMatrix[x]) - 1):

        if dataMatrix[x][y] in chars:

            # Row 1
            if dataMatrix[x-1][y-1] in numbers:
                temp.append(readNumbers(dataMatrix[x-1], y-1))

            if dataMatrix[x-1][y] in numbers:
                detectedNum = readNumbers(dataMatrix[x-1], y)
                temp.append(detectedNum) if temp[-1] != detectedNum else None

            if dataMatrix[x-1][y+1] in numbers:
                detectedNum = readNumbers(dataMatrix[x-1], y+1)
                temp.append(detectedNum) if temp[-1] != detectedNum else None

            # Row 2
            if dataMatrix[x][y-1] in numbers:
                detectedNum = readNumbers(dataMatrix[x], y-1)
                temp.append(detectedNum) if temp[-1] != detectedNum else None

            if dataMatrix[x][y+1] in numbers:
                detectedNum = readNumbers(dataMatrix[x], y+1)
                temp.append(detectedNum) if temp[-1] != detectedNum else None

            # Row 3
            if dataMatrix[x+1][y-1] in numbers:
                detectedNum = readNumbers(dataMatrix[x+1], y-1)
                temp.append(detectedNum) if temp[-1] != readNumbers else None

            if dataMatrix[x+1][y] in numbers:
                detectedNum = readNumbers(dataMatrix[x+1], y)
                temp.append(detectedNum) if temp[-1] != detectedNum else None

            if dataMatrix[x+1][y+1] in numbers:
                detectedNum = readNumbers(dataMatrix[x+1], y+1)
                temp.append(detectedNum) if temp[-1] != detectedNum else None

print(sum(temp) + 1)