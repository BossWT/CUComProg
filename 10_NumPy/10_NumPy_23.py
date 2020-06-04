import numpy as np


def read_data():
    w = [float(e) for e in input().split()]
    weight = np.array(w)
    n = int(input())
    data = np.ndarray((n, 4), int)
    for i in range(n):
        data[i] = [int(e) for e in input().split()]
    return weight, data


def report_lower_than_mean(weight, data):
    mean = np.sum(weight * data[:, 1:]) / len(data)
    res = []
    for row in data:
        score = np.sum(weight * row[1:])
        if score < mean:
            res.append(str(row[0]))
    if len(res) > 0:
        print(", ".join(res))
    else:
        print("None")


exec(input().strip())
