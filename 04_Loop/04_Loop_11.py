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
