import numpy as np
from data import nba_data, okcupid_data

nba_variance = np.var(nba_data)
okcupid_variance = np.var(okcupid_data)

# Calculate the standard deviation by taking the square root of the variance
nba_standard_deviation = nba_variance ** 0.5
okcupid_standard_deviation = okcupid_variance ** 0.5

#IGNORE CODE BELOW HERE
print("The standard deviation of the NBA dataset is " + str(nba_standard_deviation))
print("The standard deviation of the OkCupid dataset is " + str(okcupid_standard_deviation))
