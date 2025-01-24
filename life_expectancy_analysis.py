# Filename: life_expectancy_analysis.py

import codecademylib3_seaborn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the dataset
data = pd.read_csv("country_data.csv")

# Step 1: Inspect the data
print(data.head())  # Uncomment this line to view the first 5 rows of the dataset

# Step 2: Isolate the "Life Expectancy" column
life_expectancy = data["Life Expectancy"]

# Step 3: Calculate the quartiles of "Life Expectancy"
life_expectancy_quartiles = np.quantile(life_expectancy, [0.25, 0.5, 0.75])
print("Life Expectancy Quartiles:", life_expectancy_quartiles)

# Step 4: Plot a histogram of life expectancy
plt.hist(life_expectancy)
plt.title("Life Expectancy Histogram")
plt.xlabel("Life Expectancy")
plt.ylabel("Frequency")
plt.show()

# Step 6: Isolate the "GDP" column
gdp = data["GDP"]

# Step 7: Find the median GDP
median_gdp = np.median(gdp)
print("Median GDP:", median_gdp)

# Step 8: Split the dataset into low GDP and high GDP groups
low_gdp = data[data["GDP"] <= median_gdp]
high_gdp = data[data["GDP"] > median_gdp]

# Step 9: Calculate the quartiles for low GDP countries
low_gdp_quartiles = np.quantile(low_gdp["Life Expectancy"], [0.25, 0.5, 0.75])
print("Low GDP Life Expectancy Quartiles:", low_gdp_quartiles)

# Step 10: Calculate the quartiles for high GDP countries
high_gdp_quartiles = np.quantile(high_gdp["Life Expectancy"], [0.25, 0.5, 0.75])
print("High GDP Life Expectancy Quartiles:", high_gdp_quartiles)

# Step 11: Plot histograms for low and high GDP life expectancy
plt.hist(high_gdp["Life Expectancy"], alpha=0.5, label="High GDP")
plt.hist(low_gdp["Life Expectancy"], alpha=0.5, label="Low GDP")
plt.title("Life Expectancy by GDP")
plt.xlabel("Life Expectancy")
plt.ylabel("Frequency")
plt.legend()
plt.show()

# Step 12: Reflection
print("If a country has a life expectancy of 70 years:")
print(" - In the low GDP group, it falls in the second quarter.")
print(" - In the high GDP group, it falls in the first quarter.")
