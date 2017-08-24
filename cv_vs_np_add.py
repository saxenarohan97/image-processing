''' NOTE: This addition of images using OpenCV also, is not perfect!
For the right way of adding, see add_images.py
'''

import cv2
from matplotlib import pyplot as plt

path = '/Users/RohanSaxena/Documents/projects/cv'

image1 = cv2.imread(path + '/car1.png')
image2 = cv2.imread(path + '/car2.png')

np_add = image1 + image2
cv_add = cv2.add(image1, image2)

fig = plt.figure()

a = fig.add_subplot(2, 2, 1)
a.set_title('Image 1')
plt.imshow(image1)

a = fig.add_subplot(2, 2, 2)
a.set_title('Image 2')
plt.imshow(image2)

# NumPy does a modulo addition: 190 + 190 (> 255) = 380 % 255 = 125
a = fig.add_subplot(2, 2, 3)
a.set_title('NumPy')
plt.imshow(np_add)

''' ALWAYS USE OPENCV FOR ADDING IMAGES! '''
# OpenCV saturates the addition: 190 + 190 (> 255) = 255
a = fig.add_subplot(2, 2, 4)
a.set_title('OpenCV')
plt.imshow(cv_add)

plt.tight_layout()
plt.show()
