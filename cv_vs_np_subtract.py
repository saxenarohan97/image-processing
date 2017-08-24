import cv2
import numpy as np
from matplotlib import pyplot as plt

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=np.uint8)
b = np.array([[4, 5, 6], [7, 8, 9], [10, 11, 12]], dtype=np.uint8)

np_difference = a - b

cv_difference = cv2.addWeighted(a, 1, b, -1, 0)

np_difference
cv_difference

'''
What used to happen for addition occurs in subtraction also. NumPy mods values
below zero, while OpenCV truncates them to zero.
ALWAYS USE OPENCV FOR IMAGE SUBTRACTION!
'''
