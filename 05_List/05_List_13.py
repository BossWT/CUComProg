n = int(input())
ans = []
pos = 0
for i in range(n):
    num = int(input())
    if pos % 2 == 0:
        ans.append(num)
    else:
        ans.insert(0, num)
    pos += 1
num = [int(x) for x in input().split()]
for i in num:
    if pos % 2 == 0:
        ans.append(i)
    else:
        ans.insert(0, i)
    pos += 1
num = 0
while True:
    num = int(input())
    if num == -1:
        break
    if pos % 2 == 0:
        ans.append(num)
    else:
        ans.insert(0, num)
    pos += 1
print(ans)
