import cv2
from matplotlib import pyplot as plt

path = '/Users/RohanSaxena/Documents/projects/cv'

image1 = cv2.imread(path + '/car1.png')
image2 = cv2.imread(path + '/car2.png')
image3 = cv2.cvtColor(cv2.imread(path + '/pic.jpeg'), cv2.COLOR_BGR2RGB)
image4 = cv2.add(image1, image2)

images = [image1, image2, image3, image4]

'''
Use plt.tight_layout() to specify how to space the subplots in the entire
figure. It comes with some predefined parameters. See documentation for details
'''

fig = plt.figure()

names = ['Car 1', 'Car 2', 'Rohan', 'Car 1+2']

for i in range(4):

    a = fig.add_subplot(2, 2, i + 1)
    a.set_title(names[i])
    plt.imshow(images[i])

plt.tight_layout()
plt.show()
