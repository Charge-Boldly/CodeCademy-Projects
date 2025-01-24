import numpy as np
from data import dataset

# Define dataset_median here:
dataset_median = np.median(dataset)

# Ignore the code below here
try:
    print("The median of the dataset is " + str(dataset_median) + ".")
except NameError:
    print("You haven't defined dataset_median")
