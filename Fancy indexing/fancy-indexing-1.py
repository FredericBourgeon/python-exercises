"""
Fancy indexing exercise

Print #1: array([1, 12, 23, 34, 45])
Print #2: array([[30, 32, 35],
                 [40, 42, 45],
                 [50, 52, 55]])
Print #3: array([2, 22, 52])
"""

import numpy as np

a = np.arange(6) + np.arange(0, 51, 10)[:, np.newaxis]

print a[(0, 1, 2, 3, 4),(1, 2, 3, 4, 5)]
print a[3:,[0, 2, 5]]
print a[[0, 2, 5],2]