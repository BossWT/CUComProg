cards = [x for x in input().split()]
op = input().replace(' ', '')
size = len(cards) // 2
for c in op:
    card1 = cards[0:size]
    card2 = cards[size:]
    if c == 'C':
        cards = card2 + card1
    elif c == 'S':
        cards = []
        for i in range(size):
            cards.append(card1[i])
            cards.append(card2[i])
for c in cards:
    print(c, end=' ')
