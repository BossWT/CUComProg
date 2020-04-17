n = int(input())
data = []
for i in range(n):
    data.append(input().split())
info = input().split()
for i in info:
    for j in range(len(data)):
        if i not in data[j][1:]:
            data[j][0] = 0
name = {}
for i in data:
    if i[0] != 0:
        name[i[0]] = i[1:]
if not len(name):
    print('Not Found')
else:
    for k, v in sorted(name.items()):
        print(k, *v)
