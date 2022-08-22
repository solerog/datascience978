import math

from toto.divide import divide_without_raising


def test_has_correct_arithmetic():
    assert divide_without_raising(2.0, 2.0) == 1.0, 'wrong basic arithmetic'


def test_handles_divide_by_zero_correctly():
    assert divide_without_raising(2., 0.) == float('inf')
    assert divide_without_raising(-2., 0.) == -1 * float('inf')
    assert math.isnan(divide_without_raising(0., 0.))
