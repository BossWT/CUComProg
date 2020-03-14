cards = input().strip()
card = [cards[i: i + 2] for i in range(0, len(cards), 2)]
values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
suits = ['C', 'D', 'H', 'S']
for i in range(len(card) - 1):
    diffvalue = values.index(card[i][0]) - values.index(card[i + 1][0])
    diffsuit = suits.index(card[i][1]) - suits.index(card[i + 1][1])
    if diffvalue > 0:
        print('+' + str(diffvalue), end='')
    elif diffvalue < 0:
        print(diffvalue, end='')
    elif diffsuit > 0:
        print('+' + str(diffsuit), end='')
    elif diffsuit < 0:
        print(diffsuit, end='')
    else:
        print('0', end='')
