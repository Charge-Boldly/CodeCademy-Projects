# Filename: interquartile_range_analysis.py

from song_data import songs
import numpy as np

# Calculate the first quartile
q1 = np.quantile(songs, 0.25)

# Calculate the third quartile
q3 = np.quantile(songs, 0.75)

# Calculate the interquartile range
interquartile_range = q3 - q1

# Ignore the code below here
try:
    print("The first quartile of the dataset is " + str(q1) + "\n")
except NameError:
    print("You haven't defined q1 yet\n")
  
try:
    print("The third quartile of the dataset is " + str(q3) + "\n")
except NameError:
    print("You haven't defined q3 yet\n")
  
try:
    print("The IQR of the dataset is " + str(interquartile_range) + "\n")
except NameError:
    print("You haven't defined interquartile_range yet\n")
