import numpy as np
from data import nba_data, okcupid_data

# Calculate the standard deviation using NumPy's std() function
nba_standard_deviation = np.std(nba_data)
okcupid_standard_deviation = np.std(okcupid_data)

#IGNORE CODE BELOW HERE
print("The standard deviation of the NBA dataset is " + str(nba_standard_deviation))
print("The standard deviation of the OkCupid dataset is " + str(okcupid_standard_deviation))
