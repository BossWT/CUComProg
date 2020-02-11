n = [int(x) for x in input().split()]
co = 0
for i in range(len(n)):
    if i - 1 >= 0 and i + 1 < len(n):
        if n[i] > n[i - 1] and n[i] > n[i + 1]:
            co += 1
print(co)
