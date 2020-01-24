import math
a = float(input())
# U = 0
# L = 0
# while a != 0:
#     a = a // 10
#     U += 1
# x = (L + U) / 2
# print(x)
# while abs(a - x * x) > (10 ** -10) * max(a, x * x):
#     if x * x > a:
#         U = x
#     elif x * x < a:
#         L = x
#     x = (L + U) / 2
# print(x * x)
# Fuck this shit math calculation 55555555
print(round(math.log10(a), 6))
