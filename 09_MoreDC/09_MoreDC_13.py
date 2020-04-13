n = int(input())
winner = set()
loser = set()
for i in range(n):
    win, lose = input().split()
    if win not in loser:
        winner.add(win)
    loser.add(lose)
    if lose in winner:
        winner.remove(lose)
print(sorted(winner))
