#Karan Vombatkere
#University of Rochester, 2016

import numpy as np
import scipy.stats as stats


#Geometric Brownian Motion Model
#This follows the Stochastic Process dS/S = (mu)dt + (sigma)dz, dz = eps*sqrt(dt)
#Solution form, S(t) = S(t-1)*exp((mu-sigma^2/2)dt + eps*sqrt(dt)*sigma)

#Use mu = rate of return
#sigma = volatility
#dt = timestep
#Si = Initial (start) price value for each timestep
def geometric_brownian(mu, sigma, dt, Si):
    epsilon = stats.norm.rvs() #Get Normal RV with mean = 0, var=1
    Wt = epsilon*np.sqrt(dt)
    
    #calculate St
    S_t = Si*np.exp((mu-(sigma**2/2))*dt + (Wt*sigma))
    
    return S_t


#Time evolution of prices and returns
#Use the brownian motion model to generate list of prices over N days (timeperiod)
def gen_prices(mu, sigma, dt, Si, N):
    price_arr = np.zeros(N) #Initialize a vector of length N to store price values
    price_arr[0] = Si #Store first price value
    
    return_arr = np.zeros(N) #Initialize vector to store return values
    return_arr_log = np.zeros(N) #Vector to store log return values
    
    #Loop and calculate price returns between consecutive N
    for i in range (1,N):
        #Note that price[i-1] is the Si for each iteration
        price_arr[i] = geometric_brownian(mu, sigma, dt, price_arr[i-1])
        
        #R = (S(t) - S(t-1))/S(t-1)
        return_arr[i] = (price_arr[i] - price_arr[i-1])/price_arr[i-1]
        #R = log(S(t)/S(t-1))
        return_arr_log[i] = np.log((price_arr[i])/price_arr[i-1])

    
    return price_arr, return_arr, return_arr_log



#Functions to calculate return and std dev of price array
#Use to get mu_multiple and sigma_multiple
#Takes price array as input and returns mu and sigma
def avg_returns(price_array):
    mu_temp = np.zeros(len(price_array)) #Temporary array to store values
    mu_single = 0
    sigma_single = 0
    
    #Calculate the return for each iteration and store in array mu_temp
    for i in range(1,len(price_array)):
        mu_temp[i-1] = np.log(price_array[i]/price_array[i-1])
    
    #Calculate the mean return rate, mu and mean volatility, sigma of the simulation
    mu_single = np.mean(mu_temp)
    sigma_single = np.std(mu_temp)
    
    return mu_single, sigma_single


#Monte Carlo Simulations for the Geometric Brownian Motion Evolution
#Run several simulations to generate several possible price evolution arrays
#Use this to calculate the averaged volatility and return rate exhibited
def gen_multiple(mu, sigma, dt, Si, N, sim_count):
    calc_prices = np.zeros(shape=(N,sim_count)) #Create an array to store simulation values
    #For the calc_prices array we only care about the values
    #Create arrays to store values of mu and sigma for each
    mu_multiple = np.zeros(sim_count)
    sigma_multiple = np.zeros(sim_count)
    
    Nval = np.linspace(0,N-1,N)
    #Run the simulations and also plot the results of each price evolution
    plt.figure(figsize=(20,20))
    plt.title("Plot of Price Evolution, S(t) for %d Simulations" %sim_count, fontsize=16)
    plt.xlabel("N",fontsize=16)
    plt.ylabel("S(t)",fontsize=16)
    for i in range(sim_count):
        calc_prices[:,i],a,b = gen_prices(mu, sigma, dt, Si, N)
        plt.plot(Nval, calc_prices[:,i])
        
        mu_multiple[i],sigma_multiple[i] = avg_returns(calc_prices[:,i])
        
    return calc_prices, mu_multiple, sigma_multiple

