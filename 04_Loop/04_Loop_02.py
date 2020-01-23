import math
a = float(input())
L = 0
U = a
x = (L + U) / 2
while abs(a - x * x) > (10 ** -10) * max(a, x * x):
    if x * x > a:
        U = x
    elif x * x < a:
        L = x
    x = (L + U) / 2
print(round(abs(math.log10(x**2)), 6))
