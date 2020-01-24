maxzigzag = -99999
minzigzag = 99999
maxzagzig = -99999
minzagzig = 99999
i = 0
while True:
    s = input()
    if s != 'Zig-Zag' and s != 'Zag-Zig':
        x, y = s.split(' ')
        x = int(x)
        y = int(y)
        if i % 2 == 0:
            if x < minzigzag:
                minzigzag = x
            if y > maxzigzag:
                maxzigzag = y
            if x > maxzagzig:
                maxzagzig = x
            if y < minzagzig:
                minzagzig = y
        else:
            if y < minzigzag:
                minzigzag = y
            if x > maxzigzag:
                maxzigzag = x
            if y > maxzagzig:
                maxzagzig = y
            if x < minzagzig:
                minzagzig = x
    else:
        if s == 'Zig-Zag':
            print(minzigzag, maxzigzag)
        else:
            print(minzagzig, maxzagzig)
        break
    i += 1
