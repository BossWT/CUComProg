def create_dict(d, st):
    for c in st:
        if c.isalnum():
            if c not in d:
                d[c] = 1
            else:
                d[c] += 1


def comparedict(d1, d2):
    diff = {}
    for k, v in d1.items():
        if k in d2:
            diff[k] = v - d2[k]
        else:
            diff[k] = v
    return diff


def checkdiff(diff):
    ans = []
    for k, v in diff.items():
        if v > 0:
            ans.append([k, v])
    return ans


def printans(s, ans):
    print(s)
    if len(ans) == 0:
        print(' - None')
    else:
        for l, n in ans:
            print(' - remove', n, l, end='')
            if n > 1:
                print('\'s')
            else:
                print()


s1 = input()
s2 = input()
s1lower = s1.lower()
s2lower = s2.lower()
d1 = {}
d2 = {}
create_dict(d1, s1lower)
create_dict(d2, s2lower)
diff1 = comparedict(d1, d2)
diff2 = comparedict(d2, d1)
ans1 = checkdiff(diff1)
ans2 = checkdiff(diff2)
ans1.sort()
ans2.sort()
printans(s1, ans1)
printans(s2, ans2)
