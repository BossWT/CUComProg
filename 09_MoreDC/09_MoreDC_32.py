def first_fit(L, e):
    for i in range(len(L)):
        if sum(L[i]) + e <= 100:
            L[i].append(e)
            return
    L.append([e])


def best_fit(L, e):
    index = -1
    nearest = 0
    for i in range(len(L)):
        if sum(L[i]) + e <= 100:
            if sum(L[i]) + e > nearest:
                nearest = sum(L[i]) + e
                index = i
    if index == -1:
        L.append([e])
    else:
        L[index].append(e)


def partition_FF(D):
    initial = []
    initial.append([D[0]])
    for i in range(1, len(D)):
        first_fit(initial, D[i])
    return initial


def partition_BF(D):
    initial = []
    initial.append([D[0]])
    for i in range(1, len(D)):
        best_fit(initial, D[i])
    return initial


exec(input().strip())
