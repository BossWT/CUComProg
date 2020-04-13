from collections import OrderedDict
n = int(input())
userlog = OrderedDict()
citylog = OrderedDict()
for i in range(n):
    line = input()
    line = line.split(': ')
    id = line[0]
    city = line[1].split(', ')
    userlog[id] = city
    for x in city:
        if x not in citylog:
            citylog[x] = [id]
        else:
            citylog[x].append(id)
find = input()
ans = []
for x in userlog[find]:
    if x in citylog:
        for user in citylog[x]:
            if user != find and user not in ans:
                ans.append(user)
if len(ans) == 0:
    print('Not Found')
else:
    for e in userlog.keys():
        if e in ans:
            print(e)
