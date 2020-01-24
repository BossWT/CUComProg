n = int(input())
for i in range(0, n):
    for j in range(0, n - i - 1):
        print(' ', end='')
    print('*', end='')
    if i != n - 1:
        for j in range(0, 2 * i - 1):
            print(' ', end='')
        if i != 0:
            print('*', end='')
    else:
        for j in range(0, 2 * i):
            print('*', end='')
    print('')
