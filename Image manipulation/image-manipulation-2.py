# Frame Lena's face with a black locket

import numpy as np
import pylab as plt
from scipy import misc

lena = misc.lena()

# Create a non-fleshed meshgrid 512x512
x, y = np.ogrid[0:512, 0:512]
# Define the center of the image
centerx, centery = (256, 256)
# Condition for a circle of radius 230px
mask_circle = (((x - centerx)/0.6) ** 2 + ((y - centery)/1) ** 2) > 230 ** 2
# Set all pixels out of the circle to black
lena[mask_circle] = 0
plt.imshow(lena, cmap=plt.cm.gray)
plt.show()
