"""
Crude integral approximation
"""

from __future__ import division
import numpy as np


def f(a, b, c):
    """
    Return a^b - c
    """
    return a ** b - c

# Form 24x12x6 array from ranges [0, 1] x [0, 1] x [0, 1]

a, b, c = np.ogrid[0:1:24j, 0:1:12j, 0:1:6j]
my_array = f(a, b, c)

int_approx = my_array.mean() * (1 - 0) * (1 - 0) * (1 - 0)
exact_val = np.log(2) - 1 / 1/2

error = abs(exact_val - int_approx)
print 'Approximation', int_approx
print 'Exact value', exact_val
print 'Relative error', error
