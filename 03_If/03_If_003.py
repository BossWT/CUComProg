a, b, c, d = [int(e) for e in input().split()]
if a > b:
    temp = a
    a = b
    b = temp
    if d >= a:
        if c > d:
            c -= a
    else:
        c += a
    b = a + c + d
else:
    if a < c and a >= b:
        d += a
    if d > c:
        b += 2
    else:
        b *= 2
print(a, b, c, d)
