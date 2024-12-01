# Import necessary libraries
import numpy as np  # For working with arrays and numerical calculations
import pandas as pd  # For reading and handling data
import matplotlib.pyplot as plt  # For creating plots and visualizations
import seaborn as sns  # For advanced visualizations (though we may not use this here)
from scipy.stats import pearsonr  # For calculating Pearson correlation coefficient

# Set print options for NumPy to suppress scientific notation and limit precision
np.set_printoptions(suppress=True, precision=1)

# Load the penguins dataset
penguins = pd.read_csv('penguins.csv')  # Reads the CSV file and stores it in a pandas DataFrame

# Inspect the first few rows of the data to get a sense of its structure
print(penguins.head())  # Prints the first 5 rows of the dataset

# Create a scatter plot to visualize the relationship between flipper length and body mass
plt.figure(figsize=(8, 6))  # Creates a figure with a width of 8 inches and a height of 6 inches
plt.scatter(penguins['flipper_length_mm'], penguins['body_mass_g'], alpha=0.7)  
# Plots flipper_length_mm on the x-axis and body_mass_g on the y-axis as points on the graph. 
# 'alpha=0.7' makes the points a little transparent so overlapping points are visible.

# Add labels and a title to the plot for better understanding
plt.title('Flipper Length vs Body Mass')  # Title for the plot
plt.xlabel('Flipper Length (mm)')  # Label for the x-axis
plt.ylabel('Body Mass (g)')  # Label for the y-axis

# Display the plot
plt.show()  # Displays the scatter plot

# Calculate the covariance between flipper length and body mass
covariance = penguins[['flipper_length_mm', 'body_mass_g']].cov().iloc[0, 1]  
# 'cov()' calculates the covariance matrix for the selected columns.
# 'iloc[0, 1]' selects the covariance value between flipper_length_mm and body_mass_g from the matrix.

# Print the covariance result
print(f"Covariance between flipper length and body mass: {covariance}")  # Displays the covariance

# Calculate the Pearson correlation coefficient between flipper length and body mass
correlation, _ = pearsonr(penguins['flipper_length_mm'], penguins['body_mass_g'])  
# 'pearsonr' calculates the Pearson correlation coefficient, which measures the linear relationship
# between the two variables. We only need the first returned value, so we use _ for the second one.

# Print the correlation result
print(f"Pearson correlation coefficient: {correlation}")  # Displays the correlation value
