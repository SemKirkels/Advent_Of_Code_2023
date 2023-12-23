df = open('input.txt').read().split('\n')

handsAndBids = dict()

for line in df:

    tmp = [x for x in line.split(" ")]    
    handsAndBids[tmp[0]] = int(tmp[1])

def handToDict(hand):

    tmp = dict()

    for char in hand:

        if char not in tmp:
            tmp[char] = 1
        else:
            tmp[char] += 1

    return tmp

def mapToCat(hand):

    cntChars = sorted(handToDict(hand).values())
    if cntChars == [5]:
        return 1
    if cntChars == [1, 4]:
        return 2
    if cntChars == [2, 3]:
        return 3
    if cntChars == [1, 1, 3]:
        return 4
    if cntChars == [1, 2, 2]:
        return 5
    if cntChars == [1, 1, 1, 2]:
        return 6
    else:
        return 7
    
def cardsInt(hand: str) -> tuple:

    labels = 'AKQJT98765432'
    return (labels.index(card) for card in hand)

sortedHands = []

for hand in handsAndBids.keys():

    encHand = (mapToCat(hand), *cardsInt(hand), handsAndBids[hand])
    sortedHands.append(encHand)

sortedHands.sort(reverse=True)

out = 0

for i in range(1, len(sortedHands) + 1):

    out += sortedHands[i-1][-1] * i
    
print(out)
