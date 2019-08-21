# Title: Stationary Series
# Author: Danilo Pena
# Description: Stationary Time-Series

import numpy as np
import random as rd
import matplotlib.pylab as plt

# time
t = 0.001 * np.arange(1001)

# stationary
c = 0.5 # constant
sigma = 1 # N(mean, sigma)
y_ss = np.zeros(len(t))
for i in range(len(t)):
    y_ss[i] = c + rd.gauss(0, sigma) # stochastic
y_sd = np.zeros(len(t))
for i in range(1,len(t)):
    y_sd[i] = c + 0.7*y_sd[i-1] # deterministic

# non-stationary
c = 0.5 # constant
delta = 0.2
sigma = 1
y_nss = np.zeros(len(t))
for i in range(len(t)):
    y_nss[i] = c + delta*t[i] + rd.gauss(0, sigma) # stochastic with stationary trend
y_nsst = np.zeros(len(t))
for i in range(1,len(t)):
    y_nsst[i] = y_nsst[i-1] + rd.gauss(0,sigma) # stochastic with stochastic trend
y_nsd = np.zeros(len(t))
for i in range(len(t)):
    y_nsd[i] = c + delta*t[i] # deterministic

# plots
plt.subplot(2,2,1)
plt.plot(t, y_ss)
plt.title('Stationary series')
plt.xlabel('time')
plt.ylabel('y_ss')
plt.axis('tight')

plt.subplot(2,2,2)
plt.plot(t, y_sd)
plt.xlabel('time')
plt.ylabel('y_sd')
plt.axis('tight')

plt.subplot(2,2,3)
plt.plot(t, y_nss)
plt.xlabel('time')
plt.ylabel('y_nss')
plt.axis('tight')

plt.subplot(2,2,4)
plt.plot(t, y_nsd)
plt.xlabel('time')
plt.ylabel('y_nsd')
plt.axis('tight')
plt.show()



