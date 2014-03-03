"""
Mandelbrot set
Compute and plot the Mandelbrot fractal
"""

import numpy as np


def mandelbrot(N_max, some_threshold, nx,  ny):
    """
    Compute Mandelbrot's set
    """
    
    x = np.linspace(-2, 1, nx)
    y = np.linspace(-1.5, 1.5, ny)

    c = x[:, np.newaxis] + 1j*y[np.newaxis, :]
    
    z = c
    for j in xrange(N_max):
        z = z ** 2 + c

    mandelbrot_set = (abs(z) < some_threshold)
    return mandelbrot_set

mandelbrot_set = mandelbrot(50, 50, 500, 500)

import matplotlib.pyplot as plt
plt.imshow(mandelbrot_set.T, extent=[-2, 1, -1.5, 1.5])
plt.gray()
plt.savefig('mandelbrot.png')
plt.show()