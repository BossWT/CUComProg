import math
n = int(input())
low = math.sqrt(math.pi*2)*pow(n, n+0.5)*pow(math.e, (-1*n)+(1/(12*n+1)))
high = math.sqrt(math.pi*2)*pow(n, n+0.5)*pow(math.e, (-1*n)+(1/(12*n)))
print(low)
print(high)