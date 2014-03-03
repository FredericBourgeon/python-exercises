"""
Markov chain
"""

# Construct a random matrix
# Normalize each row
# Start from prob. distrib. p
# Take 50 steps
# Compute the stationary distribution

import numpy as np

n_states = 5
n_steps = 50
tolerance = 1e-5

# Create P (transition matrix) and p (prob. distrib.)
P = np.random.rand(n_states, n_states)
p = np.random.rand(n_states)

# Normalize P and p
P /= P.sum(axis=1)[:, np.newaxis]
p /= p.sum()

# Go through the damn steps
for i in xrange(n_steps):
    p = P.T.dot(p)

p_50 = p
print p_50

# Compute the stationary state
w, v = np.linalg.eig(P.T)

j_stationary = np.argmin(abs(w - 1.0))
p_stationary = v[:,j_stationary].real
p_stationary /= p_stationary.sum()
print p_stationary

# Compare
if all(abs(p_stationary - p_50) < tolerance):
    print 'In tolerance range'