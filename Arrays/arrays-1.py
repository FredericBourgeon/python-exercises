""" Create the following arrays
[[1, 1, 1, 1],
 [1, 1, 1, 1],
 [1, 1, 1, 2],
 [1, 6, 1, 1]]

[[0., 0., 0., 0., 0.],
 [2., 0., 0., 0., 0.],
 [0., 3., 0., 0., 0.],
 [0., 0., 4., 0., 0.],
 [0., 0., 0., 5., 0.],
 [0., 0., 0., 0., 6.]]

Note: par on course is 3
"""

import numpy as np

a = np.ones((4, 4), dtype=int)
a[3, 1], a[2, 3] = 6, 2

print a

b = np.zeros((6, 5))
b[1, 0], b[2, 1], b[3, 2], b[4, 3], b[5, 4] = 2, 3, 4, 5, 6

print b
