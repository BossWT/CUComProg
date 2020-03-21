def pattern1(nrows, ncols):
    ans = []
    num = 1
    for i in range(nrows):
        c = []
        for j in range(ncols):
            c.append(num)
            num += 1
        ans.append(c)
    return ans


def pattern2(nrows, ncols):
    ans = []
    for i in range(nrows):
        c = []
        num = i + 1
        for j in range(ncols):
            c.append(num)
            num += nrows
        ans.append(c)
    return ans


def pattern3(N):
    ans = []
    num = 1
    for i in range(N):
        c = []
        for j in range(i):
            c.append(0)
        for j in range(N - i):
            c.append(num)
            num += 1
        ans.append(c)
    return ans


def pattern4(N):
    ans = []
    plus = 2
    num = 1
    if N != 0:
        ans.append([num])
    for i in range(1, N):
        num += plus
        ans[0].append(num)
        plus += 1
    for i in range(1, N):
        c = []
        for j in range(i):
            c.append(0)
        for j in range(i, N):
            c.append(ans[i - 1][j] - 1)
        ans.append(c)
    return ans


def pattern5(N):
    ans = []
    plus = N
    num = 1
    if N != 0:
        ans.append([num])
    for i in range(1, N):
        num += plus
        ans[0].append(num)
        plus -= 1
    for i in range(1, N):
        c = []
        minus = N - 1
        for j in range(i):
            c.append(0)
        for j in range(i, N):
            c.append(ans[i - 1][j] - minus)
            minus -= 1
        ans.append(c)
    return ans


def pattern6(N):
    ans = [[0 for j in range(N)] for i in range(N)]
    last = int(N * (N + 1) / 2)
    row = 0
    col = 0
    rev = False
    for i in range(1, last + 1):
        # print(i, row, col)
        ans[row][col] = i
        if rev:
            direction = -1
        else:
            direction = 1
        row += direction
        col += direction
        if row == N or col == N:
            rev = True
            row -= 2
            col -= 1
        if row == -1:
            rev = False
            col += 2
            row += 1
    return ans


exec(input().strip())
