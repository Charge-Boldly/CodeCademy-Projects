from song_data import songs
import numpy as np

# Define quartiles, deciles, and tenth here:
quartiles = np.quantile(songs, [0.25, 0.5, 0.75])  # Quartiles split the dataset into 4 groups of equal size
deciles = np.quantile(songs, [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])  # Deciles split the dataset into 10 groups of equal size

# Find the tenth for a song length of 170 seconds
# Iterate through deciles to determine the correct range
tenth = None
for i in range(len(deciles)):
    if 170 <= deciles[i]:  # Check if 170 is less than or equal to the current decile value
        tenth = i + 1
        break
if tenth is None:  # If no decile matches, it falls in the final tenth
    tenth = 10

# Ignore the code below here:
try:
    print("The quartiles are " + str(quartiles) + "\n")
except NameError:
    print("You haven't defined quartiles.\n")
try:
    print("The deciles are " + str(deciles) + "\n")
except NameError:
    print("You haven't defined deciles.\n")
try:
    print("The song falls in the " + str(tenth) + "th tenth of the dataset.\n")
except NameError:
    print("You haven't defined tenth.\n")
