import numpy as np


def peak_indexes(x):
    peak = (x[1:-1] > x[:-2]) & (x[1:-1] > x[2:])
    return np.arange(1, x.size - 1)[peak]


def main():
    d = np.array([float(e) for e in input().split()])
    pos = peak_indexes(np.array(d))
    if len(pos) > 0:
        print(", ".join([str(e) for e in pos]))
    else:
        print("No peaks")


exec(input().strip())  # Don't remove this line
