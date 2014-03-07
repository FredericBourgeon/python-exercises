"""
Quiver plots
"""

import numpy as np
import pylab as pl

n = 8
X, Y = np.mgrid[0:n, 0:n]
R = 10 + np.sqrt((X - n / 2.0) ** 2 + (Y - n / 2.0) ** 2)
T = np.arctan2(Y - n / 2.0, X - n / 2.0)
U, V = R * np.cos(T), R * np.sin(T)

pl.axes([0.025, 0.025, 0.95, 0.95])
pl.quiver(X, Y, U, V, R, cmap='jet', alpha=0.5)
pl.quiver(X, Y, U, V, facecolor='none', edgecolor='black', linewidth=.5)

pl.xlim(-1, n)
pl.xticks(())
pl.ylim(-1, n)
pl.yticks(())