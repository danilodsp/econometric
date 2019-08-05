# Title: Models
# Author: Danilo Pena
# Description: Models of Hypothetical Time-Series

import numpy as np
import random as rd
import matplotlib.pylab as plt

# time
t = np.arange(101)

# the random walk hypothesis
y_rw = np.zeros(len(t))
c0 = 1
c1 = 0.2
sigma = 1
for i in range(1,len(t)):
    y_rw[i] = c0 + c1*y_rw[i-1] + rd.gauss(0,sigma)

# reduced-forms and structural equations
y_rf = np.zeros(len(t)) # GDP
c_t = np.zeros(len(t)) # consumption
i_t = np.zeros(len(t)) # investment
sigma_ct = 1
sigma_it = 1
e_ct = [rd.gauss(0,sigma_ct) for i in range(len(t))]
e_it = [rd.gauss(0,sigma_it) for i in range(len(t))]
a = 0.5 # 0<a<1
b = 0.2 # b>0
for i in range(1,len(t)):
    c_t[i] = a * y_rf[i-1] + e_ct[i] # (reduced-form equation)
    i_t[i] = b * (c_t[i] - c_t[i-1]) + e_it[i] # (structural equation)
    y_rf[i] = c_t[i] + i_t[i] # aggregate GDP
    #y_rf[i] = a * (1 + b) * y_rf[i-1] - a * b * y_rf[i-2] + (1 + b) * e_ct[i] + e_it[i] - b * e_ct[i-1] # reduced-form equation
    #y_rf[i] = c * y_rf[i-1] + d * y_rf[i-2] + disturbance # (univariate reduced-form equation), c = a*(1+b), d = -a*b, disturbance = (1+b)*e_ct[i] + e_it[i] - b*e_ct[i-1]

# error-correction: forward and spot prices
s = np.zeros(len(t)) # price of a particular foreign currency on the spot market
f = np.zeros(len(t)) # price of the currency for delivery one period into the future
sigma = 1
for i in range(1,len(t)):
    s[i] = f[i-1] + rd.gauss(0,sigma) # Unbiased Forward Rate (UFR) hypothesis
    #s[i] = a0 + a1 * f[i-1] + rd.gauss(0,sigma) # if a0=0 and a1=1 UFR hypothesis could be maintained. If rd.gauss=0, the spot and forward markets are said to be in long-run equilibrium
a = 0.5 # a>0
b = 0.6 # b>0
sigma_s = 1
sigma_f = 1
for i in range(2,len(t)): # adjustment process
    s[i] = s[i-1] - a*(s[i-1] - f[i-2]) + rd.gauss(0,sigma_s) # error-correction
    f[i-1] = f[i-2] + b*(s[i-1] - f[i-2]) + rd.gauss(0,sigma_f)

# non-linear dynamics
y_rf = np.zeros(len(t)) # GDP
c_t = np.zeros(len(t)) # consumption
i_t = np.zeros(len(t)) # investment
sigma_ct = 1
sigma_it = 1
a = 0.5 # 0<a<1
b1 = 1 # b1>0
b2 = 1 # b2>0
e_ct = [rd.gauss(0,sigma_ct) for i in range(len(t))]
e_it = [rd.gauss(0,sigma_it) for i in range(len(t))]
for i in range(1,len(t)):
    if (c_t[i] - c_t[i-1]) < 0:
        lambda_1 = 1
    else:
        lambda_1 = 0
    c_t[i] = a * y_rf[i-1] + e_ct[i]
    i_t[i] = b1 * (c_t[i] - c_t[i-1]) - lambda_1 * b2 * (c_t[i] - c_t[i-1]) + e_it[i]
    y_rf[i] = c_t[i] + i_t[i]

# plots
plt.subplot(2,2,1)
plt.plot(t,y_rw)
plt.xlabel('Time')
plt.ylabel('Random walk')
plt.axis('tight')

plt.subplot(2,2,2)
plt.plot(t,y_rf)
plt.xlabel('Time')
plt.ylabel('Keynesian model')

plt.subplot(2,2,3)
plt.plot(t,s)
plt.xlabel('Time')
plt.ylabel('Error-correction')

plt.subplot(2,2,4)
plt.plot(t,i_t)
plt.xlabel('Time')
plt.ylabel('Nonlinear dynamic')

plt.show()

