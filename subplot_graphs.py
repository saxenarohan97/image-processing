import cv2
from matplotlib import pyplot as plt

path = '/Users/RohanSaxena/Documents/projects/cv'
image = cv2.cvtColor(cv2.imread(path + '/pic.jpeg'), cv2.COLOR_BGR2RGB)

row1 = image[50, :, 0]
row2 = image[60, :, 0]

plt.subplot(2, 1, 1)
plt.plot(row1)
plt.title('Row 50')

plt.subplot(2, 1, 2)
plt.plot(row2)
plt.title('Row 60')

plt.tight_layout()
plt.show()
