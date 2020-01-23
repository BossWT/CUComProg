sum = 0.0
c = 0
while True:
    n = input()
    if n == 'q':
        break
    else:
        sum += float(n)
        c += 1
if sum == 0:
    print('No Data')
else:
    print(round(sum / c, 2))
