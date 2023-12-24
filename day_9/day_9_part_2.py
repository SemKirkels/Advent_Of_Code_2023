df = open('input.txt').read().split('\n')

def levelDown(list):

    diff = []

    for i in range(1, len(list)):

        diff.append(list[i] - list[i-1])

    return diff

out = 0
for line in df:

    parsed = [int(x) for x in line.split(" ")]
    tmp = [parsed]
    down = levelDown(parsed)

    while not all([x == 0 for x in down]):

        tmp.append(down)
        down = levelDown(down)

    for i in range(2, len(tmp) + 1):

        tmp[-i].append(tmp[-i][-1] + tmp[-i+1][-1])
        tmp[-i].insert(0, tmp[-i][0] - tmp[-i+1][0])

    # 0 to find begin
    out += tmp[0][0]

print(out)