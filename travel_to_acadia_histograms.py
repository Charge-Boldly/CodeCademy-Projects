# import codecademylib3
import codecademylib3
import numpy as np
from matplotlib import pyplot as plt

# load in data
in_bloom = np.loadtxt(open("in-bloom.csv"), delimiter=",")
flights = np.loadtxt(open("flights.csv"), delimiter=",")

# Step 1-4: Create the flights histogram
plt.figure(1)  # Create a figure for multiple subplots
plt.subplot(211)  # First subplot (2 rows, 1 column, 1st plot)

# Plot flights histogram
plt.hist(flights, range=(0, 365), bins=365)
plt.title("Flights by Day")  # Add title
plt.xlabel("Day of the Year")  # Add x-label
plt.ylabel("Flight Count")  # Add y-label

# Step 5-6: Prepare for second subplot
plt.subplot(212)  # Second subplot (2 rows, 1 column, 2nd plot)

# Step 7-8: Plot in_bloom histogram
plt.hist(in_bloom, range=(0, 365), bins=365)
plt.title("Flowers Blooming by Day")  # Add title for second plot
plt.xlabel("Day of the Year")  # Add x-label
plt.ylabel("Bloom Count")  # Add y-label

# Step 8: Adjust layout to prevent overlap
plt.tight_layout()

# Display the plots
plt.show()
