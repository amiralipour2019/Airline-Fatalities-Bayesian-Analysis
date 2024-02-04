# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 14:04:08 2024

@author: Amir Alipour
"""

#Load the libraries
import numpy as np
from scipy.stats import gamma, poisson
import pandas as pd

# create fatal airline data 
airline_fatalities = {
    "Year": [1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985],
    "Fatal Accidents": [24, 25, 31, 31, 22, 21, 26, 20, 16, 22],
    "Passenger Deaths": [734, 516, 754, 877, 814, 362, 764, 809, 223, 1066],
    "Death Rate (per 100 million passenger miles)": [0.19, 0.12, 0.15, 0.16, 0.14, 0.06, 0.13, 0.13, 0.03, 0.15]
}

# Creating a DataFrame
fatal_df= pd.DataFrame(airline_fatalities )
fatal_df

# Given posterior parameters for theta (from the Gamma distribution)
alpha_posterior = 239 
beta_posterior = 10.1  

# Number of simulations
num_simulations = 10000

# Simulate samples from the posterior distribution of theta
theta_samples = gamma.rvs(alpha_posterior, scale=1/beta_posterior, size=num_simulations)

theta_samples
# Simulate Poisson distributed number of accidents for each theta sample
accident_samples = [poisson.rvs(mu=theta) for theta in theta_samples]

# Calculate the 2.5th and 97.5th percentiles
lower_percentile = np.percentile(accident_samples, 2.5)
upper_percentile = np.percentile(accident_samples, 97.5)

(lower_percentile, upper_percentile)






# Calculating exposure (passenger miles flown)
# Since the death rate is per 100 million passenger miles, we multiply by 100 million
fatal_df["Exposure (passenger miles flown)"] = fatal_df["Passenger Deaths"] /fatal_df["Death Rate (per 100 million passenger miles)"] * 100000000

fatal_df.round(2)  # Rounding off to two decimal places for display purposes

sum_exposure= np.sum(np.array([fatal_df["Exposure (passenger miles flown)"]]))
sum_exposure



# Posterior parameters for theta
alpha_prime = 239
beta_prime = 5.72e12

# Number of simulations
num_simulations = 10000

# Assume 8 x 10^11 passenger miles flown in 1986
w = 8e11

# Simulate samples from the posterior distribution of theta
theta_samples2 = gamma.rvs(alpha_prime, scale=1/beta_prime, size=num_simulations)

theta_samples2
# Simulate Poisson distributed number of accidents for each theta sample
accident_samples2 = [poisson.rvs(mu=theta * w) for theta in theta_samples2]
accident_samples2
# Calculate the 95% predictive interval
lower_percentile_2 = np.percentile(accident_samples2, 2.5)
upper_percentile_2 = np.percentile(accident_samples2, 97.5)

(lower_percentile_2, upper_percentile_2)


# Given posterior parameters for theta (from the Gamma distribution)

alpha_posterior_update =1+ fatal_df["Passenger Deaths"].sum()
 
beta_posterior_update = 10.1 

# Number of simulations
num_simulations = 10000

# Simulate samples from the posterior distribution of theta
theta_samples_update= gamma.rvs(alpha_posterior_update, scale=1/beta_posterior_update, size=num_simulations)

theta_samples_update
# Simulate Poisson distributed number of accidents for each theta sample
accident_samples_update = [poisson.rvs(mu=theta) for theta in theta_samples_update]

# Calculate the 2.5th and 97.5th percentiles
lower_percentile_update = np.percentile(accident_samples_update, 2.5)
upper_percentile_update = np.percentile(accident_samples_update, 97.5)

(lower_percentile_update, upper_percentile_update)




# Calculating exposure (passenger miles flown)
# Since the death rate is per 100 million passenger miles, we multiply by 100 million
fatal_df["Exposure_accidents"] = fatal_df["Fatal Accidents"] /fatal_df["Death Rate (per 100 million passenger miles)"] * 100000000

fatal_df.round(2)  # Rounding off to two decimal places for display purposes

sum_exposure_accidents= fatal_df["Exposure_accidents"].sum()
sum_exposure_accidents
# Expressing the number in scientific notation
scientific_notation = "{:.2e}".format(sum_exposure_accidents+0.1)

scientific_notation


# Posterior parameters for theta
alpha_prime = 238
beta_prime = 2.28e11

# Number of simulations
num_simulations = 10000

# Assume 8 x 10^11 passenger miles flown in 1986
w = 8e11

# Simulate samples from the posterior distribution of theta
theta_samples2 = gamma.rvs(alpha_prime, scale=1/beta_prime, size=num_simulations)

theta_samples2
# Simulate Poisson distributed number of accidents for each theta sample
accident_samples2 = [poisson.rvs(mu=theta * w) for theta in theta_samples2]
accident_samples2
# Calculate the 95% predictive interval
lower_percentile_2 = np.percentile(accident_samples2, 2.5)
upper_percentile_2 = np.percentile(accident_samples2, 97.5)

(lower_percentile_2, upper_percentile_2)
