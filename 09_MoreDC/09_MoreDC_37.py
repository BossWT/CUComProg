n = int(input())
dept = {}
for i in range(n):
    d, amount = input().split()
    dept[d] = int(amount)
n = int(input())
std = {}
for i in range(n):
    data = input().split()
    std[data[0]] = [float(data[1]), data[2:]]
ans = {}
for k, v in sorted(std.items(), key=lambda x: -1 * x[1][0]):
    for select in v[1]:
        if dept[select] > 0:
            ans[k] = select
            dept[select] -= 1
            break
for k, v in sorted(ans.items()):
    print(k, v)
