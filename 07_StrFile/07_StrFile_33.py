def readfile(path):
    f = open(path, 'r')
    res = []
    for line in f:
        temp = line.split()
        res.append([temp[0][-2:], temp[0], temp[1]])
    res.sort()
    return res


path1, path2 = input().split()
combine = readfile(path1) + readfile(path2)
combine.sort()
for faculty, id, grade in combine:
    print(id, grade)
