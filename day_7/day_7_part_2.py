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

def mapToCategory(hand):

    jokers = hand.count('J')
    fixedHand = [c for c in hand if c != 'J']
    cntChars = sorted(handToDict(fixedHand).values())

    if not cntChars:
        cntChars = [0] 
    if cntChars[-1] + jokers == 5:
        return 1
    if cntChars[-1] + jokers == 4:
        return 2
    if cntChars[-1] + jokers == 3 and cntChars[-2] == 2:
        return 3
    if cntChars[-1] + jokers == 3:
        return 4
    if cntChars[-1] == 2 and (jokers or cntChars[-2] == 2):
        return 5
    if cntChars[-1] == 2 or jokers:
        return 6
    else:
        return 7
    
def cardsInt(hand: str) -> tuple:

    labels = 'AKQT98765432J'
    return (labels.index(card) for card in hand)

sortedHandsJoker = []

for hand in handsAndBids.keys():

    encHand = (mapToCategory(hand), *cardsInt(hand), handsAndBids[hand])
    sortedHandsJoker.append(encHand)

sortedHandsJoker.sort(reverse=True)

out = 0

for i in range(1, len(sortedHandsJoker) + 1):

    out += sortedHandsJoker[i-1][-1] * i

print(out)