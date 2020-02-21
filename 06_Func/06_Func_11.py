a, b = input().split()
a = int(a, 2)
b = int(b, 2)
sum = a + b
ans = bin(sum)
print(ans[2:])
