st = input()
num = []
for c in st:
    if c.isdigit() and int(c) not in num:
        num.append(int(c))
if len(num) == 10:
    print('None')
else:
    co = 10 - len(num)
    r = 0
    for i in range(10):
        if i not in num:
            print(i, end='')
            r += 1
            if r != co:
                print('', end=',')
