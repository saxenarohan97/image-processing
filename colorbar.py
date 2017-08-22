import matplotlib.pyplot as plt
import cv2

path = '/Users/RohanSaxena/Documents/projects/cv'
image = cv2.imread(path + '/pic.jpeg')

blue = image[:, :, 0]
green = image[:, :, 1]
red = image[:, :, 2]

fig = plt.figure()
# Where to put ticks on the colorbar:
tick_list = [0, 30, 60, 90, 130, 170, 210]

a = fig.add_subplot(2, 2, 1)
plt.imshow(blue, cmap='Blues')
a.set_title('Blue')
plt.colorbar(ticks=tick_list, orientation='horizontal')

a = fig.add_subplot(2, 2, 2)
plt.imshow(green, cmap='Greens')
a.set_title('Green')
plt.colorbar(ticks=tick_list, orientation='horizontal')

a = fig.add_subplot(2, 2, 3)
plt.imshow(red, cmap='Reds')
a.set_title('Red')
plt.colorbar(ticks=tick_list, orientation='horizontal')

plt.show()
