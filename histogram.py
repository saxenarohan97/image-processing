import numpy as np
from matplotlib import pyplot as plt
from matplotlib import mlab as mlab

x = np.random.randn(10000)

bins = plt.hist(x, 50, normed=True, facecolor='green', alpha=0.75)[1]

y = mlab.normpdf(bins, 0, 1)

plt.plot(bins, y, 'r', linewidth=2)
plt.xlabel('Value')
plt.ylabel('Probability')
plt.axis([-4, 4, 0, 0.45])
plt.grid(True)

plt.show()
