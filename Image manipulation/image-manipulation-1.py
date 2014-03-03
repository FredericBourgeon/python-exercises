"""
Image manipulation
"""

from scipy import misc
import pylab as plt

lena = misc.lena() # Load Lena
plt.imshow(lena)   # Show the image
plt.show()         # Open in new window

plt.imshow(lena, cmap=plt.cm.gray) # Map the image to grayscale
plt.show()                         # Open in new window

crop_lena = lena[30:-30,30:-30]    # Remove 30 pixels from all sides
plt.imshow(crop_lena)              # Show the image
plt.show()                         # Open in new window
