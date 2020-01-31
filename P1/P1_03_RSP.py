m = int(input())
wina = 0
winb = 0
ro = 0
while wina != m and winb !=m and ro!=3*m:
    a,b = input().split(' ')
    if a=='R' and b == 'P':
        winb +=1
    elif a=='P' and b == 'R':
        wina +=1
    elif a == 'R' and b == 'S':
        wina +=1
    elif a == 'S' and b == 'R':
        winb +=1
    elif a == 'S' and b == 'P':
        wina += 1
    elif a == 'P' and b == 'S':
        winb += 1
    ro+=1
print(wina,winb)
if wina == winb or (wina != m and winb != m):
    print('Tie')
elif wina > winb:
    print("Player 1 wins")
elif(winb > wina):
    print("Player 2 wins")