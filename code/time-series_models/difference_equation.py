# Title: Difference Equation
# Description: First code here
# Author: Danilo Pena

import numpy as np
import random as rd
import matplotlib.pylab as plt

# time
#t = range(101)
t = np.arange(101)

# trend
T = 1 + 0.1*t
# seasonal
S = 1.6*np.sin(t*np.pi/6)
# irregular
I = np.zeros(len(t))
rd.seed(1)
for i in range(2,len(t)):
    I[i] = 0.7*I[i-1] + rd.random()

y = T + S + I

plt.plot(t, y)
plt.xlabel('Months')
plt.ylabel('y')
plt.axis('tight')
plt.show()

