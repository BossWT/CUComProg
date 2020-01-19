num = [float(e) for e in input().split()]
num.sort()
ans = (num[1] + num[2]) / 2
print(round(ans, 2))
