from song_data import songs
import numpy as np

# Step 1: Calculate the first quartile
songs_q1 = np.quantile(songs, 0.25)

# Step 2: Calculate the second and third quartile
songs_q2 = np.quantile(songs, 0.50)
songs_q3 = np.quantile(songs, 0.75)

# Step 3: Look up the length of your favorite song in seconds
favorite_song = 240  # Replace 240 with the length of your favorite song in seconds

# Determine the quarter where the favorite song falls
if favorite_song <= songs_q1:
    quarter = 1
elif favorite_song <= songs_q2:
    quarter = 2
elif favorite_song <= songs_q3:
    quarter = 3
else:
    quarter = 4

# Ignore the code below here:
try:
    print("The first quartile of dataset one is " + str(songs_q1) + " seconds")
except NameError:
    print("You haven't defined songs_q1")
try:
    print("The second quartile of dataset one is " + str(songs_q2) + " seconds")
except NameError:
    print("You haven't defined songs_q2")
try:
    print("The third quartile of dataset one is " + str(songs_q3) + " seconds")
except NameError:
    print("You haven't defined songs_q3\n")

print(f"Your favorite song falls in quarter {quarter} of the data.")
