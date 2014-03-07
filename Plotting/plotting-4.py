"""
Contour plots
"""

import numpy as np
import pylab as pl


def f(x, y):
    return (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x ** 2 - y ** 2)

n = 256
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)
X, Y = np.meshgrid(x, y)

pl.axes([0.025, 0.025, 0.95, 0.95])
pl.contourf(X, Y, f(X, Y), 8, alpha=0.75, cmap='hot')
C = pl.contour(X, Y, f(X, Y), 8, colors='black', linewidth=0.5)
pl.clabel(C)

pl.xticks(())
pl.yticks(())