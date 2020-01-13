a = input()
b = input()
sa = a[1:-1:]
sb = b[1:-1:]
u = sa.split(', ')
v = sb.split(', ')
u = list(map(float, u))
v = list(map(float, v))
ans = [x + y for x, y in zip(u, v)]
print(u, end=" + ")
print(v, end=" = ")
print(ans)
