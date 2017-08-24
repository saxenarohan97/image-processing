import cv2
import numpy as np
from numpy.random import normal
from matplotlib import pyplot as plt

path = '/Users/RohanSaxena/Documents/projects/cv'
image = cv2.cvtColor(cv2.imread(path + '/pic.jpeg'), cv2.COLOR_BGR2RGB)

row = image[60, :, 0]

plt.subplot(2, 1, 1)
plt.plot(row)
plt.xlabel('Column')
plt.ylabel('Pixel')
plt.title('Original row')

noise = normal(scale=10, size=np.shape(row))

noisy_row = row + noise
plt.subplot(2, 1, 2)
plt.plot(noisy_row)
plt.xlabel('Column')
plt.ylabel('Pixel')
plt.title('Noisy row')

plt.tight_layout()
plt.show()
