import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# Load the dataset
sleep = pd.read_csv('sleep_performance.csv')

# Create the scatter plot
plt.scatter(sleep.hours_sleep, sleep.performance)  # Plot hours_sleep on the x-axis and performance on the y-axis
plt.xlabel('Hours of Sleep')  # Label for the x-axis
plt.ylabel('Performance Score')  # Label for the y-axis
plt.title('Scatter Plot of Hours of Sleep vs. Performance')  # Title of the plot

# Display the plot
plt.show()

# Calculate the correlation between hours_sleep and performance
corr_sleep_performance, p_value = pearsonr(sleep.hours_sleep, sleep.performance)

# Print the correlation result
print("Pearson correlation coefficient between hours of sleep and performance:", corr_sleep_performance)


