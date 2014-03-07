"""
Text plot
"""

import pylab as pl
import numpy as np

txts = []
txts.append((r"$W^{3\beta}_{\delta_1 \rho_1 \sigma_2} = U^{3\beta}_{\delta_1 \rho_1} + \frac{1}{8 \pi 2} \int^{\alpha_2}_{\alpha_2} d \alpha^\prime_2 \left[\frac{ U^{2\beta}_{\delta_1 \rho_1} - \alpha^\prime_2U^{1\beta}_{\rho_1 \sigma_2} }{U^{0\beta}_{\rho_1 \sigma_2}}\right]$"))
txts.append((r"$\frac{d\rho}{d t} + \rho \vec{v}\cdot\nabla\vec{v} = -\nabla p + \mu\nabla^2 \vec{v} + \rho \vec{g}$"))
txts.append((r"$\int_{-\infty}^\infty e^{-x^2}dx=\sqrt{\pi}$"))
txts.append((r"$E = mc^2 = \sqrt{{m_0}^2c^4 + p^2c^2}$"))
txts.append((r"$F_G = G\frac{m_1m_2}{r^2}$"))

for i in range(20):
    index = np.random.randint(0, len(txts))
    txt = txts[index]
    size = np.random.uniform(12, 32)
    alpha = np.random.uniform(0.25, 0.75)
    x, y = np.random.uniform(0, 1, 2)
    pl.text(x, y, txt, va='center', ha='center', fontsize=size, color="#11557c", alpha=alpha, clip_on=True)
pl.xticks(())
pl.yticks(())
pl.show()
