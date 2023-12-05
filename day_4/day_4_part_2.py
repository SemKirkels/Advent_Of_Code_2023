df = open('input.txt', 'r').read().split('\n')
scratch = dict()
numScratch = 0

for i in range(len(df)):

    row = df[i].split(":")[1]
    winRow = [int(x.strip()) if x != '' else None for x in row.split('|')[0].split(' ')]
    myRow = [int(x.strip()) if x!= '' else None for x in row.split('|')[1].split(' ')]
    scratch[i+1] = {'num': 1, 'win': 0}

    for num in myRow:
        if num in winRow and num is not None:
            scratch[i+1]['win'] += 1

for card in scratch:
    for i in range(scratch[card]['win']):

        try:
            scratch[card+i+1]['num'] += scratch[card]['num']
        except:
            continue

for card in scratch:
    numScratch += scratch[card]['num']

print(numScratch)   