import numpy as np


def mult_table(nrows, ncols):
    rows = np.arange(1, nrows + 1)
    cols = np.arange(1, ncols + 1)
    return np.outer(rows, cols)


exec(input().strip())
