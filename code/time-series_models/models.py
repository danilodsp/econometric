# Title: Models
# Author: Danilo Pena
# Description: Models of Hypothetical Time-Series

import numpy as np
import random as rd
import matplotlib.pylab as plt

# time
t = np.arange(101)

# the random walk hypothesis
y = np.zeros(len(t))
c0 = 1
c1 = 0.2
sigma = 1
for i in range(1,len(t)):
    y[i] = c0 + c1*y[i-1] + rd.gauss(0,sigma)

# plots
plt.plot(t,y)
plt.xlabel('time')
plt.ylabel('random walk')
plt.axis('tight')
plt.show()

