import numpy as np
# A is a 2-d array


def get_column_from_bottom_to_top(A, c):
    res = A[::-1]
    res = np.dstack(res)
    return res[0][c]


def get_odd_rows(A):
    return A[1::2]


def get_even_column_last_row(A):
    res = A[-1]
    return res[::2]


def get_diagonal1(A):  # A is a square matrix
    return np.diag(A)


def get_diagonal2(A):  # A is a square matrix
    return np.fliplr(A).diagonal()


exec(input().strip())
