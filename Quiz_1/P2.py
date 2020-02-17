x = [int(e) for e in input().split()]
k = int(input())
n = len(x)
i = 0
sum = 0
while i < n:
    count = 1
    j = i
    while j + 1 < n and x[j] == x[j + 1]:
        count += 1
        j += 1
    if count < k:
        sum += x[i] * count
    i += count
print(sum)
