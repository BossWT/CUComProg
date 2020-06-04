import numpy as np


def sum_2_rows(M):
    res = []
    for i in range(0, len(M), 2):
        res.append(M[i] + M[i + 1])
    return np.array(res)


def sum_left_right(M):
    res = []
    for i in range(0, len(M) // 2):
        res.append(M[:, i] + M[:, len(M) // 2 + i])
    return np.transpose(res)


def sum_upper_lower(M):
    half = np.vsplit(M, 2)
    return np.array([half[0][i] + half[1][i] for i in range(len(half[0]))])


def sum_4_quadrants(M):
    halfv = np.vsplit(M, 2)
    halfh = np.array([np.hsplit(halfv[0], 2), np.hsplit(halfv[1], 2)])
    return np.array((halfh[0][0] + halfh[0][1]) + (halfh[1][0] + halfh[1][1]))


def sum_4_cells(M):
    halfv = np.vsplit(M, len(M) / 2)
    halfh = np.array([np.hsplit(r, len(M) / 2) for r in halfv])
    res = []
    for i in halfh:
        row = []
        for j in i:
            row.append(np.sum(j))
        res.append(row)
    return np.array(res)


def count_leap_years(years):
    count = 0
    for y in years:
        if ((y - 543) % 4 == 0 and (y - 543) % 100 != 0) or (y - 543) % 400 == 0:
            count += 1
    return count


exec(input().strip())
