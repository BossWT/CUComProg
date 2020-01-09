m = input()
n = int(input())
l = len(m)
le = max(l,n)
z = le-l
for i in range(0,z):
    print('0',end='')
print(m)