"""
Leibniz formula for Pi
Computes Pi using a summation
This formula converges slowly
"""

from __future__ import division

n = int(raw_input('How many terms in the summation? '))

my_pi = 0

for i in range(0, n):
    my_pi += (- 1) ** i / (2 * i + 1)

my_pi *= 4

print my_pi
