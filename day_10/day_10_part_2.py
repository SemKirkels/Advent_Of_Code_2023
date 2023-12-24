df = open("input.txt")

grid: list[str] = df.readlines()

up: list[chr] = ['|', 'F', '7']
down: list[chr] = ['|', 'J', 'L']
left: list[chr] = ['-', 'F', 'L']
right: list[chr] = ['-', '7', 'J']

def getTiles(grid: list[str]) -> dict:

    def at(grid: list[str], pos: tuple[int,int]) -> chr: return grid[pos[1]][pos[0]]
    def move(pos: tuple[int,int], dir: tuple[int,int]) -> tuple[int, int]: return (pos[0] + dir[0], pos[1] + dir[1])
    def inbounds(grid: list[str], pos: tuple[int,int]) -> bool: return pos[1] >= 0 and pos[0] >= 0 and pos[1] < len(grid) and pos[0] < len(grid[0])
    def canMove(curPos: tuple[int,int], dir: tuple[int,int], prevPos: tuple[int,int], valid_tiles: list[chr]) -> bool:
        newPos: tuple[int,int] = move(curPos, dir)
        return at(grid, curPos) in valid_move.get(dir) and newPos != prevPos and inbounds(grid, newPos) and at(grid, newPos) in valid_tiles
        
    row: int = 0
    col: int = 0
    found_S: bool = False
    S: tuple[int, int] = (0,0)

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            tile: chr = grid[row][col].strip()
            if tile == 'S':
                found_S = True
                S = (col, row)
                break
        if found_S:
            break

    valid_move: dict = {

        (0,-1) : ['S', '|', 'L', 'J'],
        (-1,0) : ['S', '7', '-', 'J'],
        (+1,0) : ['S', 'F', '-', 'L'],
        (0,+1) : ['S', '|', 'F', '7']
    }

    prevPos: tuple[int,int] = (-1,-1)
    curPos: tuple[int,int] = S
    tiles: dict = {S : 'S'}

    while True:

        if canMove(curPos, (0,-1), prevPos, up):
            prevPos = curPos
            curPos = move(curPos, (0,-1))

        elif canMove(curPos, (-1,0), prevPos, left):
            prevPos = curPos
            curPos = move(curPos, (-1,0))

        elif canMove(curPos, (+1,0), prevPos, right):
            prevPos = curPos
            curPos = move(curPos, (+1,0))

        elif canMove(curPos, (0,+1), prevPos, down):
            prevPos = curPos
            curPos = move(curPos, (0,+1))

        else:
            break
        
        tiles[curPos] = at(grid, curPos)
    
    return tiles

cTiles: dict = getTiles(grid)

posPoints: list[tuple[int,int]] = []

for row in range(len(grid)):

    for col in range(len(grid[0].strip())):

        if (col,row) not in cTiles.keys():
            posPoints.append((col,row))

inPoints: int = 0

for point in posPoints:

    (x,y) = point[0], point[1]-1
    inter: list[chr] = []

    while y >= 0:
        if (x,y) in cTiles.keys() and cTiles[(x,y)] != '|':
            
            if cTiles[(x,y)] != 'S':
                inter.append(cTiles[(x,y)])

            elif cTiles.get((x-1,y)) in left:
                inter.append('7')

            elif cTiles.get((x+1,y)) in right:
                inter.append('F')

        y-=1

    nInter: int = 0
    i: int = 0

    while i < len(inter):

        if inter[i] == '-' or inter[i+1] == '-':
            nInter += 1
            i+=1

        elif (i+1 >= len(inter) or
            inter[i] == 'F' and inter[i+1] == 'J' or
            inter[i] == 'J' and inter[i+1] == 'F' or
            inter[i] == '7' and inter[i+1] == 'L' or
            inter[i] == 'L' and inter[i+1] == '7'):

            nInter += 1
            i+=2

        else:
            nInter += 2
            i+=2

    if nInter % 2 != 0:
        inPoints += 1

print(inPoints)