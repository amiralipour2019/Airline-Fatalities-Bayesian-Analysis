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
1. Download `BM-HW2.py` from this repository.
2. Open a terminal or command prompt.
3. Navigate to the directory containing `BM-HW2.py`.
4. Execute the script with Python:

### Expected Output
The script outputs analyses of the airline fatalities dataset, including Bayesian estimates and visualizations of posterior distributions for key variables. These insights help understand the variability and underlying trends in aviation safety data.

## Dataset
The included dataset is a dictionary in the script, detailing yearly data on fatal accidents, passenger deaths, and death rates per 100 million passengers. This data serves as the foundation for the Bayesian analysis.

### Modifying the Dataset
To analyze different data:
- Modify the `airline_fatalities` dictionary within `BM-HW2.py` to reflect your dataset.
- Ensure your data includes "Year", "Fatal Accidents", "Passenger Deaths", and "Death Rate (per 100 million passengers)".
- Rerun the script to analyze the new data with the Bayesian model.

## Data Analysis
The script utilizes Bayesian modeling to estimate parameters of interest, performing posterior simulations to understand the probability distributions of aviation safety metrics. This method provides a nuanced view of the data, highlighting potential safety trends and areas for improvement.

## Contributing
Contributions are welcome! If you have suggestions for improving this analysis or have found a bug, please:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a new Pull Request.

