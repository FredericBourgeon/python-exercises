"""
Array manipulations
"""

import numpy as np

# Number 1

# Array a goes from 1 to 15, spanning on three columns

a = np.arange(1, 16).reshape((3, 5)).T

print 'Number 1' + '\n'

print a

# Array b contains only 2nd and 4th rows

b = a.copy()[1::2]

print b

# Number 2

c = np.arange(25).reshape(5, 5)
d = np.arange(0., 21, 5)[:, np.newaxis]
d[0] = 1

e = c / d

print '\n' + 'Number 2' + '\n'

print e

# Number 3

f = np.random.rand(10, 3)
g = f[range(10), np.abs(f - 0.5).argsort()[:, 0]]

print '\n' + 'Number 3' + '\n'

print f
print g