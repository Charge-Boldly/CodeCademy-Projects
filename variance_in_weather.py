# Import necessary libraries for working with data
import codecademylib3_seaborn  # Codecademy's library for visualization and tools
import pandas as pd  # Library for handling structured data like tables
import numpy as np  # Library for numerical computations

# Import the dataset containing London weather data
from weather_data import london_data  # london_data is provided as a DataFrame

# Task 1: Display the first few rows of the dataset
# Use the head() function to inspect the first rows of the dataset.
print(london_data.head())  # Shows the structure of the data, including its columns.

# Task 2: Calculate the number of data points in the dataset
# len() gives the total number of rows in the DataFrame.
print(len(london_data))  # Prints the total count of weather measurements.

# Task 3: Extract the "TemperatureC" column
# Use bracket notation to select the "TemperatureC" column from the dataset.
temp = london_data["TemperatureC"]  # Stores all temperature data from the dataset.

# Task 4: Calculate the mean (average) temperature
# np.mean computes the average value of the temperature data.
average_temp = np.mean(temp)  # Calculates and stores the average temperature.
print("Average Temperature:", average_temp)  # Prints the result.

# Task 5: Calculate the variance of temperature
# Variance shows how spread out the temperatures are around the average.
temperature_var = np.var(temp)  # Calculates the variance.
print("Temperature Variance:", temperature_var)  # Prints the variance.

# Task 6: Calculate the standard deviation of temperature
# Standard deviation gives an idea of how much temperatures deviate from the average.
temperature_standard_deviation = np.std(temp)  # Calculates the standard deviation.
print("Temperature Standard Deviation:", temperature_standard_deviation)  # Prints it.

# Task 7: Filter data by the month of June
# Use loc[] to filter rows where the "month" column equals 6 (June).
june = london_data.loc[london_data["month"] == 6]["TemperatureC"]  # June's temperatures.

# Task 8: Filter data by the month of July
# Similarly, filter rows where the "month" column equals 7 (July).
july = london_data.loc[london_data["month"] == 7]["TemperatureC"]  # July's temperatures.

# Task 9: Calculate and compare average temperatures for June and July
# Compute the mean temperature for June and July using np.mean().
june_mean = np.mean(june)  # Average temperature in June.
july_mean = np.mean(july)  # Average temperature in July.
print("June Mean Temperature:", june_mean)  # Print June's average temperature.
print("July Mean Temperature:", july_mean)  # Print July's average temperature.

# Task 10: Compare standard deviations for June and July
# Calculate the standard deviation for June and July temperatures.
june_std = np.std(june)  # Standard deviation of temperatures in June.
july_std = np.std(july)  # Standard deviation of temperatures in July.
print("June Temperature Standard Deviation:", june_std)  # Print June's deviation.
print("July Temperature Standard Deviation:", july_std)  # Print July's deviation.

# Task 11: Print mean and standard deviation for all months
# Loop through each month (1 to 12) and calculate statistics.
for i in range(1, 13):  # Loop over months 1 (January) to 12 (December)
    month = london_data.loc[london_data["month"] == i]["TemperatureC"]  # Filter for each month.
    print(f"The mean temperature in month {i} is {np.mean(month)}")  # Print monthly mean.
    print(f"The standard deviation of temperature in month {i} is {np.std(month)}\n")  # Print std dev.

# Task 12: Explore other insights (Optional, for further analysis)
# Example: Identify the month with the least variable temperature
# and analyze other columns like humidity or air pressure if desired.
