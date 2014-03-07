"""
Pie charts
"""

import numpy as np
import pylab as pl

n = 20
Z = np.ones(n)
Z[-1] *= 2
pl.pie(Z, explode=Z*0.05, colors=[str((i/float(n))) for i in range(n)])

pl.axis('equal')
pl.xticks(())
pl.yticks(())

