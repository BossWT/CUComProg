a = input().split(' ')
b = input().split(' ')
mon = ['January',
       'February',
       'March',
       'April',
       'May',
       'June',
       'July',
       'August',
       'September',
       'October',
       'November',
       'December']
if int(a[3]) < int(b[3]):
    print(a[0])
elif int(b[3]) < int(a[3]):
    print(b[0])
else:
    mona = mon.index(a[1])
    monb = mon.index(b[1])
    if mona < monb:
        print(a[0])
    elif monb < mona:
        print(b[0])
    else:
        daya = a[2][0:-1]
        dayb = b[2][0:-1]
        if int(daya) < int(dayb):
            print(a[0])
        elif int(dayb) < int(daya):
            print(b[0])
        else:
            print(a[0], b[0])
