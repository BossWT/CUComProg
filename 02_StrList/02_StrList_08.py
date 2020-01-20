import math
n, d, r = [a for a in input().split(',')]
if r == '':
    num = int(n + d)
    denom = len(d)
    denom = 10 * denom
else:
    num = int(n + d + r) - int(n + d)
    denom = len(r) * '9' + len(d) * '0'
    denom = int(denom)
if denom == 0:
    denom = 1
gcd = math.gcd(num, denom)
print(int(num // gcd), '/', int(denom // gcd))
