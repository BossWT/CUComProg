rotate = input()
row = int(input())
msg = []
flag = False
for i in range(row):
    st = input().strip()
    if i == 0:
        length = len(st)
    if length != len(st):
        flag = True
    else:
        msg.append(st)
column = length
if not flag:
    if rotate == '90':
        for i in range(column):
            for j in range(row):
                print(msg[row - j - 1][i], end='')
            print('')
    elif rotate == 'flip':
        for i in range(row):
            for j in range(column):
                print(msg[i][column - j - 1], end='')
            print('')
    elif rotate == '180':
        for i in range(row):
            for j in range(column):
                print(msg[row - i - 1][column - j - 1], end='')
            print('')
else:
    print('Invalid size')
