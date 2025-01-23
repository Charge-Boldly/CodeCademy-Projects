import codecademylib3_seaborn
from song_data import songs
import matplotlib.pyplot as plt

# Find the maximum and minimum values of the dataset
maximum = max(songs)
minimum = min(songs)

# Calculate the range of the dataset
song_range = maximum - minimum

# Ignore the code below here
plt.hist(songs, bins=200)
plt.xlabel("Song Length (Seconds)")
plt.ylabel("Count")
plt.show()

try:
    print("The range of the dataset is " + str(song_range) + " seconds")
except NameError:
    print("You haven't defined the variable song_range yet")
