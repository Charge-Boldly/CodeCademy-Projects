# Import packages
import numpy as np
import pandas as pd

# Array of days old bread
days_old_bread = np.array([0, 8, 7, 8, 0, 2, 3, 5, 6, 2])

# Set the minimum and maximums of the array below
min_days_old = np.min(days_old_bread)  # Calculate the minimum value in the array
max_days_old = np.max(days_old_bread)  # Calculate the maximum value in the array

# Set the number of bins to 3
bins = 3  # Number of bins for the histogram

# Calculate the bin range
try:
    bin_range = (max_days_old - min_days_old + 1) / bins  # Calculate the width of each bin
    print("Bins: " + str(bins))  # Print the number of bins
    print("Bin Width: " + str(bin_range))  # Print the bin width
except:
    print("You have not set the min, max, or bins values yet.")  # Fallback error message
