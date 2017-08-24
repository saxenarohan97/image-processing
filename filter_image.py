import cv2
from matplotlib import pyplot as plt

path = '/Users/RohanSaxena/Documents/projects/cv'
image = cv2.cvtColor(cv2.imread(path + '/pic.jpeg'), cv2.COLOR_BGR2RGB)

# Blur an image using a Gaussian filter

blurred1 = cv2.GaussianBlur(image, (11, 11), 3)
blurred2 = cv2.GaussianBlur(image, (31, 31), 3)

fig = plt.figure()

a = fig.add_subplot(1, 2, 1)
plt.imshow(blurred1)
a.set_title('11 x 11')

a = fig.add_subplot(1, 2, 2)
plt.imshow(blurred2)
a.set_title('31 x 31')

plt.tight_layout()
plt.show()
