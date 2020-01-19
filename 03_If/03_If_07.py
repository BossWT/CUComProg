n = input()
if len(n) < 4:
    print(n)
elif len(n) < 7:
    temp = float(n)
    temp /= 1000
    if temp < 10:
        print(str(round(temp, 1)) + 'K')
    else:
        print(str(round(temp)) + 'K')
elif len(n) < 10:
    temp = float(n)
    temp /= 1e6
    if temp < 10:
        print(str(round(temp, 1)) + 'M')
    else:
        print(str(round(temp)) + 'M')
else:
    temp = float(n)
    temp /= 1e9
    if temp < 10:
        print(str(round(temp, 1)) + 'B')
    else:
        print(str(round(temp)) + 'B')
