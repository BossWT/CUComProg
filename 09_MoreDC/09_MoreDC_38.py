station = {}
now = ''
while True:
    data = input().split()
    if len(data) == 1:
        now = data[0]
        break
    if data[0] not in station:
        station[data[0]] = set([data[1]])
    else:
        station[data[0]].add(data[1])
    if data[1] not in station:
        station[data[1]] = set([data[0]])
    else:
        station[data[1]].add(data[0])
ans = set()
ans.add(now)
if now in station:
    for st in station[now]:
        ans.add(st)
        for st2 in station[st]:
            ans.add(st2)
for x in sorted(ans):
    print(x)
