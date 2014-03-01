"""
Leibniz formula for Pi
Computes Pi using a summation
This formula converges slowly
One line function
"""

from __future__ import division

n = int(raw_input('How many terms in the summation? '))

print 4 * reduce(lambda x, y: x + y,
                 [(-1)**i/(2*i+1)
                  for i in range(0, n)])
