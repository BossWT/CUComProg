import numpy as np
import math


def toCelsius(f):
    return (f - 32) * 5 / 9


def BMI(wh):
    return np.array([w / (h / 100 * h / 100) for w, h in wh])


def distanceTo(p, Points):
    return np.array([math.sqrt((x - p[0])**2 + (y - p[1])**2) for x, y in Points])


exec(input().strip())
