# Bayesian Modeling for Airline Fatalities Analysis

## Description
This project employs Bayesian modeling and posterior simulation to analyze trends in airline fatalities over several years. Written in Python, it leverages statistical methods to estimate distributions related to fatal accidents, passenger deaths, and death rates. The goal is to gain insights into the effectiveness of aviation safety measures and predict future trends based on historical data.

## Prerequisites
- Python 3.x
- Libraries: numpy, scipy, pandas

## Setup
1. Ensure Python 3.x is installed on your system.
2. Install the required Python libraries using pip:

## Running the Script
1. Download `Airline-Fatalities-Bayesian-Analysis.py` from this repository.
2. Open a terminal or command prompt.
3. Navigate to the directory containing `Airline-Fatalities-Bayesian-Analysis.py`.
4. Execute the script with Python:

### Expected Output
The script outputs analyses of the airline fatalities dataset, including Bayesian estimates and visualizations of posterior distributions for key variables. These insights help understand the variability and underlying trends in aviation safety data.

## Dataset
The dataset used in this project details worldwide airline fatalities from 1976 to 1985, focusing on the number of fatal accidents, passenger deaths, and the death rate (passenger deaths per 100 million passenger miles). This comprehensive dataset is sourced from the Statistical Abstract of the United States, providing a reliable basis for our Bayesian analysis.
### Modifying the Dataset
To analyze different data:
- Modify the `airline_fatalities` dictionary within `Airline-Fatalities-Bayesian-Analysis.py` to reflect your dataset.
- Ensure your data includes "Year", "Fatal Accidents", "Passenger Deaths", and "Death Rate (per 100 million passengers)".
- Rerun the script to analyze the new data with the Bayesian model.

## Data Analysis
The script utilizes Bayesian modeling to estimate parameters of interest, performing posterior simulations to understand the probability distributions of aviation safety metrics. This method provides a nuanced view of the data, highlighting potential safety trends and areas for improvement.


