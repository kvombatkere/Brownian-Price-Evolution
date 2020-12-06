#Karan Vombatkere
#University of Rochester, 2016

import numpy as np
import scipy.stats as stats

from BrownianModel import *

#Run a single simulation to check functionality 
#Test with sample values for mu, sigma and Si
mu = 0.15
sigma = 0.07
Si = 100
N = 500
dt = 0.01

#Call Function
Slist, Rlist, Rloglist = gen_prices(mu, sigma, dt, Si, N)
Nval = np.linspace(0,N-1,N)

#Plot results
plt.figure(figsize=(15,5))
plt.title("Plot of Price Evolution for 1 simulation", fontsize=14)
plt.xlabel("N",fontsize=16)
plt.ylabel("S(t)",fontsize=16)
plt.plot(Nval,Slist)

plt.figure(figsize=(15,5))
plt.title("Plot of Price Distribution for 1 simulation", fontsize=14)
plt.xlabel("Price Level",fontsize=16)
plt.ylabel("R(t)",fontsize=16)
n, bins, patches=plt.hist(Slist,bins=50,normed=1,label="S")

#Plot returns
plt.figure(figsize=(15,5))
plt.title("Plot of Returns and Log Returns Distribution for 1 simulation", fontsize=14)
plt.xlabel("Return",fontsize=16)
plt.ylabel("Frequency",fontsize=16)
n, bins, patches=plt.hist(Rloglist,bins=50,normed=1,label="Log(R)")
n, bins, patches=plt.hist(Rlist,bins=50,normed=1,label="R")