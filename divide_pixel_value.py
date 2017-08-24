import cv2
import numpy as np
from matplotlib import pyplot as plt

path = '/Users/RohanSaxena/Documents/projects/cv'

image = cv2.imread(path + '/car1.png')

fig = plt.figure()

a = fig.add_subplot(2, 2, 1)
plt.imshow(image)
a.set_title('Image')

'''
Diving an image by 2 converts it to float32. See data_type.py as to why this is
a problem.
'''
a = fig.add_subplot(2, 2, 2)
plt.imshow(image / 2)
a.set_title('Image / 2')

'''
To divide pixel values, make sure you convert back to the original data type,
or better yet use the cv2.addWeighted() function
'''
a = fig.add_subplot(2, 2, 3)
plt.imshow((image / 2).astype(np.uint8))
a.set_title('Image / 2 -> uint8')

a = fig.add_subplot(2, 2, 4)
plt.imshow(cv2.addWeighted(image, 0.25, image, 0.25, 0))
a.set_title('Add Weighted')

plt.tight_layout()
plt.show()
