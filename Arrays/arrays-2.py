"""
Create the following array using numpy.tile
[[4, 3, 4, 3, 4, 3],
 [2, 1, 2, 1, 2, 1],
 [4, 3, 4, 3, 4, 3],
 [2, 1, 2, 1, 2, 1]]
"""

import numpy as np

base = np.array([[4, 3], [2, 1], [4, 3], [2, 1]])

print np.tile(base, 3)
