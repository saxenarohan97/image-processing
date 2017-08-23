import matplotlib.pyplot as plt
import cv2

path = '/Users/RohanSaxena/Documents/projects/cv'
image = cv2.imread(path + '/pic.jpeg')

blue = image[:, :, 0]
green = image[:, :, 1]
red = image[:, :, 2]

fig = plt.figure()

a = fig.add_subplot(1, 3, 1)
imgplot = plt.imshow(blue, cmap='Blues')
a.set_title('Blue')

a = fig.add_subplot(1, 3, 2)
imgplot = plt.imshow(green, cmap='Greens')
a.set_title('Green')

a = fig.add_subplot(1, 3, 3)
imgplot = plt.imshow(red, cmap='Reds')
a.set_title('Red')

plt.tight_layout()
plt.show()
