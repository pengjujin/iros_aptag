import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
import math

mu1 = 1
variance1 = 0.3
sigma1 = math.sqrt(variance1)
x1 = np.linspace(-5, 15, 700)
y1 = mlab.normpdf(x1, mu1, sigma1) / 2
# plt.plot(x1,y1)
# lt.fill(x1, y1, color='black', facecolor='red', alpha=0.5)

mu2 = 8
variance2 = 0.3
sigma2 = math.sqrt(variance2)
x2 = np.linspace(-5, 15, 700)
y2 = mlab.normpdf(x2, mu2, sigma2) / 2
plt.plot(x1, y1, x2,y2, color = 'red')
plt.fill(x1, y1, facecolor='red', alpha=0.5)
plt.fill(x2, y2, facecolor='red', alpha=0.5)
plt.show()

