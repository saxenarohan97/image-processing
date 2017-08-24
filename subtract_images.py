import cv2
from matplotlib import pyplot as plt

'''
To subtract images properly, use one of the following:
(i)     (a - b) + (b - a) if both images a and b are uint8
(ii)    Convert to floating-point
'''

path = '/Users/RohanSaxena/Documents/projects/cv'

image1 = cv2.imread(path + '/car1.png')
image2 = cv2.imread(path + '/car2.png')

difference1 = cv2.addWeighted(image1, 1, image2, -1, 0)
difference2 = cv2.addWeighted(image1, -1, image2, 1, 0)
net_difference = cv2.addWeighted(image1, 1, image2, 1, 0)

plt.imshow(net_difference)
plt.show()
