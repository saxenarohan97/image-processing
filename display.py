import cv2
import matplotlib.pyplot as plt

path = '/Users/RohanSaxena/Documents/projects/cv'
image = cv2.imread(path + '/pic.jpeg')

''' We need to do the following conversion because openCV reads in an RGB
image's pixel values as BGR values. See channel.py for doing this manually '''
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()
