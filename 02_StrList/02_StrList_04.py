m = input()
n = int(input())
x = len(m)
le = max(x, n)
z = le - x
for i in range(0, z):
    print('0', end='')
print(m)
