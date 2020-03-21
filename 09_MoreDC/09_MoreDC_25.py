def row_number(t, e):  # return row number of t containing e (top row is row #0)
    for x in range(len(t)):
        if e in t[x]:
            return x


def flatten(t):  # return a list of ints converted from list of lists of ints t
    ans = []
    for i in t:
        for j in i:
            if j != 0:
                ans.append(j)
    return ans


def inversions(x):  # return the number of inversions of list x
    inverse = 0
    for i in range(len(x)):
        for j in range(i + 1, len(x)):
            if x[i] > x[j]:
                inverse += 1
    return inverse


def solvable(t):  # return True if tiling t (list of lists of ints) is solvable
    rows = len(t)
    flat = flatten(t)
    inverse = inversions(flat)
    if rows % 2 == 1:
        if inverse % 2 == 0:
            return True
    else:
        if inverse % 2 == 1:
            if row_number(t, 0) % 2 == 0:
                return True
        else:
            if row_number(t, 0) % 2 == 1:
                return True
    return False


exec(input().strip())  # do not remove this line
