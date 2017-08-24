import cv2
from matplotlib import pyplot as plt

path = '/Users/RohanSaxena/Documents/projects/cv'

image1 = cv2.imread(path + '/car1.png')
image2 = cv2.imread(path + '/car2.png')

'''
Adding 2 images with the brightest pixels will result in a pixel having twice
the maximum brightness. To resolve this, average the 2 images.
'''

addition = cv2.add(image1, image2)
normalised = cv2.addWeighted(image1, 0.5, image2, 0.5, 0)

fig = plt.figure()

a = fig.add_subplot(2, 2, 1)
plt.imshow(image1)
a.set_title('Image 1')

a = fig.add_subplot(2, 2, 2)
plt.imshow(image2)
a.set_title('Image 2')

a = fig.add_subplot(2, 2, 3)
plt.imshow(addition)
a.set_title('Un-normalised')

a = fig.add_subplot(2, 2, 4)
plt.imshow(normalised)
a.set_title('Normalised')

plt.tight_layout()
plt.show()
