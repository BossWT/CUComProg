import math
n = int(input())
data = []
for i in range(n):
    x, y = input().split()
    x = float(x)
    y = float(y)
    dist = math.sqrt(x * x + y * y)
    payload = [dist, i + 1, x, y]
    data.append(payload)
data.sort()
print('#' + str(data[2][1]) + ': ' + '(' + str(data[2][2]) + ', ' + str(data[2][3]) + ')')
