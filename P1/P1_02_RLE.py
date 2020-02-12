op = input()
if op == 'str2RLE':
    st = input()
    co = 1
    ans = ''
    temp = st[0]
    if len(st) == 1:
        print(st, '1')
    else:
        for i in range(1, len(st)):
            if st[i] == temp:
                co += 1
            else:
                ans += temp + ' ' + str(co) + ' '
                co = 1
            if i == len(st) - 1:
                ans += st[i] + ' ' + str(co)
            temp = st[i]
        print(ans)
elif op == 'RLE2str':
    st = input().split(' ')
    for i in range(0, len(st), 2):
        print(st[i] * int(st[i + 1]), end='')
else:
    print('Error')
