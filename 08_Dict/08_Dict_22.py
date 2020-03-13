n = int(input())
d_icecream = {}
d_total = {}
maxsale = -9999
sum = 0.0
for i in range(n):
    name, price = input().split()
    d_icecream[name] = price
m = int(input())
for i in range(m):
    name, amount = input().split()
    amount = int(amount)
    if name in d_icecream:
        if name in d_total:
            d_total[name] += int(d_icecream[name]) * amount
        else:
            d_total[name] = int(d_icecream[name]) * amount
        maxsale = max(d_total[name], maxsale)
        sum += int(d_icecream[name]) * amount
d_total = {k: v for k, v in sorted(d_total.items(), key=lambda item: item[1], reverse=True)}
ans = {}
for k, v in d_total.items():
    if v == maxsale:
        ans[k] = v
if sum == 0:
    print('No ice cream sales')
else:
    print('Total ice cream sales:', sum)
    print('Top sales: ', end='')
    ans = sorted(ans.keys())
    for i in range(len(ans)):
        print(ans[i], end='')
        if i != len(ans) - 1:
            print(end=', ')
