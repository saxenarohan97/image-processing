import cv2
import matplotlib.pyplot as plt

path = '/Users/RohanSaxena/Documents/projects/cv'
image = cv2.imread(path + '/pic.jpeg')

# Cropping images is just slicing NumPy arrays
crop = image[5:130, 60:165, :]

plt.imshow(crop)
plt.show()

'''
The first dimension is the height, starting from the top.
The second dimension is the width, starting from the left.
So this is proper matrix coordinates: row-column form.
'''
