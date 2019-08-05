# Title: Stationary Series
# Author: Danilo Pena
# Description: Stationary Time-Series

import numpy as np
import random as rd
import matplotlib.pylab as plt

# time
t = np.arange(1001)

# stationary
c = 0.8 # constant
sigma = 1 # N(mean, sigma)
y_ss = np.zeros(len(t))
for i in range(len(t)):
    y_ss[i] = c + rd.gauss(0, sigma) # stochastic
y_sd = np.zeros(len(t))
for i in range(1,len(t)):
    y_sd[i] = c + 0.5*y_sd[i-1] # deterministic

# non-stationary
c = 0.8 # constant
delta = 1
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



