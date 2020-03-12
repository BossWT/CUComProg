n = int(input())
full = {}
for i in range(n):
    nick, real = input().split()
    full[nick] = real
rfull = {}
for nick, real in full.items():
    rfull[real] = nick
n = int(input())
ans = []
for i in range(n):
    name = input()
    if name in full:
        print(full[name])
    elif name in rfull:
        print(rfull[name])
    else:
        print('Not found')
