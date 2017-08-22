import cv2
import numpy as np
from matplotlib import pyplot as plt

path = '/Users/RohanSaxena/Documents/projects/cv'
image = cv2.imread(path + '/pic.jpeg')
print(np.shape(image))

# A single pixel value
print(image[100, 100])

# An entire row of pixel values from blue channel
some_blue_pixels = image[:, 100, 0]

# An entire row of pixel values from the picture
image[:, 100, :]

plt.plot(range(212), some_blue_pixels)
plt.axis([0, 212, 0, 170])
plt.show()
