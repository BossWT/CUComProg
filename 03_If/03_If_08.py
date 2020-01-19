d = int(input())
m = int(input())
y = int(input())
ans = 0
day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
y -= 543
if y % 400 == 0:
    day[2] = 29
if y % 4 == 0 and y % 100 != 0:
    day[2] = 29
for i in range(1, m):
    ans += day[i]
ans += d
print(ans)
