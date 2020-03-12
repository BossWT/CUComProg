str = input()
str = str.lower()
d = {}
for c in str:
    if c.isalpha():
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
nd = []
for k, v in d.items():
    nd.append([-v, k])
nd.sort()
for n, c in nd:
    print(c, '->', -n)
