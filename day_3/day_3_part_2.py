fd = open("input.txt")

dataMatrix = [line for line in fd]
chars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '/', '?', '<', '>']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
temp = []

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

        if dataMatrix[x][y] == "*":
            
            temp_2 = [-1]

            if dataMatrix[x-1][y-1] in numbers:
                temp_2.append(readNumbers(dataMatrix[x-1], y-1))

            if dataMatrix[x-1][y] in numbers:
                detected_number = readNumbers(dataMatrix[x-1], y)
                temp_2.append(detected_number) if temp_2[-1] != detected_number else None

            if dataMatrix[x-1][y+1] in numbers:
                detected_number = readNumbers(dataMatrix[x-1], y+1)
                temp_2.append(detected_number) if temp_2[-1] != detected_number else None

            if dataMatrix[x][y-1] in numbers:
                detected_number = readNumbers(dataMatrix[x], y-1)
                temp_2.append(detected_number) if temp_2[-1] != detected_number else None

            if dataMatrix[x][y+1] in numbers:
                detected_number = readNumbers(dataMatrix[x], y+1)
                temp_2.append(detected_number) if temp_2[-1] != detected_number else None

            if dataMatrix[x+1][y-1] in numbers:
                detected_number = readNumbers(dataMatrix[x+1], y-1)
                temp_2.append(detected_number) if temp_2[-1] != detected_number else None

            if dataMatrix[x+1][y] in numbers:
                detected_number = readNumbers(dataMatrix[x+1], y)
                temp_2.append(detected_number) if temp_2[-1] != detected_number else None

            if dataMatrix[x+1][y+1] in numbers:
                detected_number = readNumbers(dataMatrix[x+1], y+1)
                temp_2.append(detected_number) if temp_2[-1] != detected_number else None

            temp_2.pop(0)
            if len(temp_2) == 2:
                temp.append(temp_2[0]*temp_2[1])

print(sum(temp))