def convex_polygon_area(p):
    p.append([p[0][0], p[0][1]])
    down = 0
    up = 0
    for i in range(len(p) - 1):
        downx = p[i][0]
        downy = p[i + 1][1]
        upx = p[i + 1][0]
        upy = p[i][1]
        down += downx * downy
        up += upx * upy
    area = 0.5 * (down - up)
    return abs(area)


def is_heterogram(s):
    d = {}
    s = s.lower()
    for c in s:
        if c.isalpha():
            if c in d:
                return False
            else:
                d[c] = 1
    return True


def replace_ignorecase(s, a, b):
    text = s.lower()
    check = a.lower()
    start = text.find(check)
    index = start
    found = []
    while index != -1:
        found.append(index)
        start = index + len(check)
        index = text.find(check, start)
    ans = ''
    i = 0
    while i < len(s):
        if i in found:
            ans += b
            i += len(a)
        else:
            ans += s[i]
            i += 1
    return ans


def top3(votes):
    ans = []
    for keys, value in votes.items():
        ans.append([-value, keys])
    ans.sort()
    res = []
    for n in range(len((ans))):
        if n == 3:
            break
        res.append(ans[n][1])
    return res


for k in range(2):
    exec(input().strip())
