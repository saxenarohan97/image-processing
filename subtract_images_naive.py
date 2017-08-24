import cv2
from matplotlib import pyplot as plt

path = '/Users/RohanSaxena/Documents/projects/cv'

image1 = cv2.imread(path + '/car1.png')
image2 = cv2.imread(path + '/car2.png')

# Always use OpenCV for image subtraction. See cv_vs_np_subtract.py
difference1 = cv2.addWeighted(image1, 1, image2, -1, 0)
difference2 = cv2.addWeighted(image2, 1, image1, -1, 0)

'''
In image difference, brighter areas in the result indicate a higher degree of
difference between the 2 images.
'''

fig = plt.figure()

a = fig.add_subplot(1, 2, 1)
imgplot = plt.imshow(difference1)
a.set_title('Image 1 - 2')

a = fig.add_subplot(1, 2, 2)
imgplot = plt.imshow(difference2)
a.set_title('Image 2 - 1')

plt.tight_layout()
plt.show()

'''
The 2 results difference1 & difference2 will be different since the pixel
value p1 - p2 is different from p2 - p1.
'''
