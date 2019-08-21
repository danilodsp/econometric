# Title: Cobweb model
# Author: Danilo Pena
# Description: Traditional Cobweb model

import numpy as np
import random as rd
import matplotlib.pylab as plt

# time
t = np.arange(101)

d = np.zeros(len(t)) # demand for wheat in period t
s = np.zeros(len(t)) # supply of wheat in t
p = np.zeros(len(t)) # market price of wheat in t
pe = np.zeros(len(t)) # price that farmers expect to prevail at t

sigma = 0.01 # variance of supply shock

# parameters (guess)
a = 4 # a>b
b = 2 # b>0
gamma = 1 # gamma>0
beta = 1 # beta>0

p[0] = (a-b)/(gamma+beta) # initial condition

for i in range(1,len(t)):
    e = rd.gauss(0,sigma)
    #p[i] = (a-b)/(gamma+beta) # just a test, force to equilibrium
    p[i] = (-beta/gamma)*p[i-1] + (a-b)/gamma - e/gamma

    d[i] = a - gamma*p[i]
    s[i] = b + beta*pe[i] + e
    
    pe[i] = p[i-1] # in the case of using last year's price as the expected market price
    
    if d[i] == s[i]:
        print("d = s = %d" % d[i])

plt.plot(s,p)
plt.ylabel('Price')
plt.xlabel('Quantity')
plt.title('Cobweb model')
plt.show()

