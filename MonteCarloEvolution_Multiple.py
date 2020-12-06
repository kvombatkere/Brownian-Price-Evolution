#Karan Vombatkere
#University of Rochester, 2016

import numpy as np
import scipy.stats as stats

from BrownianModel import *

#Run multiple Monte Carlo Simulations
#Test with sample values for mu, sigma and Si
#Run multiple simulations with sample values for the input parameters
mu = 0.15
sigma = 0.07
Si = 100
N = 500
dt = 0.01
sim_count = 500

#Call the function and run the simulations
prices_multiple, mu_arr, sigma_arr = gen_multiple(mu, sigma, dt, Si, N, sim_count)