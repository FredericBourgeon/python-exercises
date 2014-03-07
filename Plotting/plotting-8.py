"""
Grids
"""

import pylab as pl

axes = pl.gca()
axes.set_xlim(0, 4)
axes.set_ylim(0, 3)
axes.xaxis.set_major_locator(pl.MultipleLocator(1.0))
axes.xaxis.set_minor_locator(pl.MultipleLocator(0.1))
axes.yaxis.set_major_locator(pl.MultipleLocator(1.0))
axes.yaxis.set_minor_locator(pl.MultipleLocator(0.1))
axes.set_xticklabels([])
axes.set_yticklabels([])
pl.grid(1, which='major', linewidth=1.0, linestyle='-', alpha=0.5)
pl.grid(1, which='minor', linewidth=0.5, linestyle='-', alpha=0.5)