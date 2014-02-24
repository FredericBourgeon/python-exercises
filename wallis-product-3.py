########################################
## Wallis product - Pi approximation
## Simple algorithm as a one-liner
########################################

from __future__ import division

## Pi 100 first decimals (generated by Wolfram Mathematica)
pi = 3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117068

n = int(raw_input('How many terms? '))

print pi
print 2 * reduce(lambda x, y: x * y, [((4 * i ** 2) / (4 * i ** 2 - 1)) for i in range(1, n)])