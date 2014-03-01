"""
Compute prime numbers in 0 - 99
"""

import numpy as np

is_prime = np.ones((100,), dtype=bool)

# Cross-out 0 and 1
is_prime[:2] = 0

N_max = int(np.sqrt(len(is_prime)))
for j in range(2, N_max):
    is_prime[j*j::j] = False

prime = np.nonzero(is_prime)

for j in prime:
    print j
