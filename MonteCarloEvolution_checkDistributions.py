#Karan Vombatkere
#University of Rochester, 2016

import numpy as np
import scipy.stats as stats

from BrownianModel import *

#Plot the distributions of the price levels and returns to check the validity of simulations
#Price Levels should be lognormally distributed according to Geometric Brownian Motion Model
#Return Rate and Volatility should be normally distributed

#Plot Price Levels
plt.figure(figsize=(15,5))
plt.title("Distribution of Price Levels for %d Simulations" %sim_count, fontsize=16)
plt.xlabel("Price",fontsize=16)
plt.ylabel("Frequency, P(x)",fontsize=16)
n, bins, patches=plt.hist(prices_multiple, bins=100,normed=1,label="R")

#Compare with Lognormal distribution with Mean and Stdev given below
lognorm_mean = Si*np.exp(mu*N*dt)
lognorm_var = (Si**2)*np.exp(2*mu*N*dt)*(np.exp((sigma**2)*N*dt)-1)
s,loc,scale = stats.lognorm.fit(prices_multiple)
lognorm_dist = stats.lognorm.pdf(bins,s,loc,scale)
plt.plot(bins,lognorm_dist,"g",lw=5,label="Lognormal PDF")  #plot the expected lognormal density distribution

#Plot the return and volatility distribution
plt.figure(figsize=(15,5))
plt.title("Distribution of Return Rates for %d Simulations" %sim_count, fontsize=16)
plt.xlabel("Return Rate, $\mu$",fontsize=16)
plt.ylabel("Frequency, P(x)",fontsize=16)
n, bins, patches=plt.hist(mu_arr,bins=100,normed=1,label="R")

plt.figure(figsize=(15,5))
plt.title("Distribution of Volatility for %d Simulations" %sim_count, fontsize=16)
plt.xlabel("Volatility, $\sigma$",fontsize=16)
plt.ylabel("Frequency, P(x)",fontsize=16)
n, bins, patches=plt.hist(sigma_arr,bins=100,normed=1,label="sigma")