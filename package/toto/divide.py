from ast import Raise
from math import isnan
import ipdb


def divide_without_raising(x: float, y: float) -> float:
    '''
    divides x by y and returns if y equals 0:
    - inf if x positive
    - -inf if x negative
    - nan if x equals 0
    '''
    if y == 0:
        if x > 0:
            return float('inf')
        if x < 0:
            return float('inf')
        return float('nan')
    return x / y


divide_without_raising(1, 1)
