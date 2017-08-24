import cv2
from matplotlib import pyplot as plt

path = '/Users/RohanSaxena/Documents/projects/cv'

image = cv2.imread(path + '/car1.png')

fig = plt.figure()

a = fig.add_subplot(1, 3, 1)
plt.imshow(image)
a.set_title('Original image')

'''
While multiplying an image by a scalar, the same problem will occur that occurs
while adding images: NumPy will mod values over 255 while OpenCV will truncate
them. ALWAYS USE OPENCV TO MULTIPLY AN IMAGE BY A SCALAR!
'''

a = fig.add_subplot(1, 3, 2)
plt.imshow(cv2.addWeighted(image, 2, image, 0, 0))
a.set_title('OpenCV multiplication')

a = fig.add_subplot(1, 3, 3)
plt.imshow(image * 2)
a.set_title('Image * 2')

plt.tight_layout()
plt.show()
