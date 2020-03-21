score = {'X': 0, 'R': 1, 'Y': 2, 'G': 3, 'W': 4, 'B': 5, 'P': 6, 'K': 7}
point = [0, 0]
while True:
    plus = 0
    play = input().strip()
    player = int(play[0])
    for i in range(1, len(play)):
        plus += score[play[i]]
    point[player - 1] += plus
    if play[1] == 'K':
        print(point[0], point[1])
        if point[1] > point[0]:
            print('Player 2 wins')
        elif point[0] > point[1]:
            print('Player 1 wins')
        else:
            print('Tie')
        break
