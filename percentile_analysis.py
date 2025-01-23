from song_data import songs
import numpy as np

# Define percentile and answer here:
percentile = np.quantile(songs, 0.32)  # 32nd percentile
three_minute_song = 180  # Song length in seconds (3 minutes)

if three_minute_song > percentile:
    answer = "above"
else:
    answer = "below"

# Ignore the code below here:
try:
    print("Your percentile is " + str(percentile) + "\n")
except NameError:
    print("You haven't defined percentile")
