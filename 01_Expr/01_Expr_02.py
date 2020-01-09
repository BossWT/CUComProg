import math
a = float(input())
b = float(input())
c = float(input())
x = ((-1*b)-math.sqrt(pow(b, 2)-(4*a*c)))/(2*a)
y = ((-1*b)+math.sqrt(pow(b, 2)-(4*a*c)))/(2*a)
print(round(x, 3))
print(round(y, 3))