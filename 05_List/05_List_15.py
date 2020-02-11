n = [int(x) for x in input().split()]
n.sort()
num = []
ans = []
count = 1
# This comment is timeout method
# for i in n:
#     if i not in num:
#         if len(ans) < 10:
#             ans.append(i)
#         num.append(i)
#         count += 1
ans.append(n[0])
for i in range(1, len(n)):
    if n[i] != n[i - 1]:
        if len(ans) < 10:
            ans.append(n[i])
        count += 1
print(count)
print(ans)
