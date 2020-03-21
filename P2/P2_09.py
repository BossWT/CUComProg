def show(data):
    for e in data:
        print(*e)


def get(vitamin, fruit):
    print(fruit, end=' ')
    if fruit in vitamin:
        print(*vitamin[fruit])
    else:
        print('not found')


def avg(vitamin, vit):
    total = 0
    n = 0
    for k, v in vitamin.items():
        total += v[vit - 1]
        n += 1
    ans = total / n
    print(round(ans, 4))


def maxvit(vitamin, vit):
    maximum = -9999
    ans = []
    for k, v in vitamin.items():
        if v[vit - 1] >= maximum:
            maximum = v[vit - 1]
            ans.append([-v[vit - 1], k])
    ans.sort()
    print(ans[0][1], -ans[0][0])


def sortvit(vitamin, vit):
    ans = []
    for k, v in vitamin.items():
        ans.append([v[vit - 1], k])
    ans.sort()
    for e in ans:
        print(e[1], end=' ')


vitamin = {}
n = int(input())
data = []
for i in range(n):
    payload = input()
    payload = payload.split()
    data.append(payload)
    name = payload[0]
    for i in range(1, len(payload)):
        payload[i] = float(payload[i])
    vitamin[name] = payload[1:]
cmd = input().split()
if cmd[0] == 'show':
    show(data)
elif cmd[0] == 'get':
    get(vitamin, cmd[1])
elif cmd[0] == 'avg':
    avg(vitamin, int(cmd[1]))
elif cmd[0] == 'max':
    maxvit(vitamin, int(cmd[1]))
elif cmd[0] == 'sort':
    sortvit(vitamin, int(cmd[1]))
