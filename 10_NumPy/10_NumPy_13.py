import numpy as np
import math


def p(X):
    return np.array([1 / (1 + math.e**(-(-3.98 + 0.1 * x + 0.5 * y))) for x, y in X])


exec(input().strip())
