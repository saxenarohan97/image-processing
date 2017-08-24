import cv2
import numpy as np
from matplotlib import pyplot as plt

path = '/Users/RohanSaxena/Documents/projects/cv'

image = cv2.imread(path + '/car1.png')
float_image = image.astype(np.float32)

'''
Different data types expect pixel values to be in different ranges. Be careful
while converting from one data type to the other.
'''

fig = plt.figure()

a = fig.add_subplot(1, 2, 1)
plt.imshow(image)
a.set_title('uint8 Image')

a = fig.add_subplot(1, 2, 2)
plt.imshow(float_image)
a.set_title('float32 Image')

plt.tight_layout()
plt.show()
