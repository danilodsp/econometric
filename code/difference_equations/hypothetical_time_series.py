# Title: Difference Equation
# Author: Danilo Pena
# Description: Hypothetical Time-Series

import numpy as np
import random as rd
import matplotlib.pylab as plt

# time
t = np.arange(101)

# trend component
T = 1 + 0.1*t
# seasonal component
S = 1.6*np.sin(t*np.pi/6)
# irregular component
I = np.zeros(len(t))
rd.seed(1)
for i in range(2,len(t)):
    I[i] = 0.7*I[i-1] + rd.random()

# complete signal
y = T + S + I

# plot y
plt.plot(t, y)
plt.xlabel('Months')
plt.ylabel('y')
plt.axis('tight')
plt.show()

