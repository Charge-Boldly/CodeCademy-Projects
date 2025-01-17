# Importing the numpy library to use its built-in functions
import numpy as np

# Define a list of grades (our dataset)
grades = [88, 82, 85, 84, 90]

# Calculate the average (mean) of the grades using numpy's mean function
mean = np.mean(grades)

# Compute the difference between the first grade and the mean
difference_one = grades[0] - mean

# Compute the difference between the second grade and the mean
difference_two = grades[1] - mean

# Compute the difference between the third grade and the mean
difference_three = grades[2] - mean

# Compute the difference between the fourth grade and the mean
difference_four = grades[3] - mean

# Compute the difference between the fifth grade and the mean
difference_five = grades[4] - mean

# Print the mean of the dataset
print("The mean of the data set is " + str(mean) + "\n")

# Print how far the first grade is from the mean, rounded to 2 decimal places
print("The first student is " + str(round(difference_one, 2)) + " percentage points away from the mean.")

# Print how far the second grade is from the mean, rounded to 2 decimal places
print("The second student is " + str(round(difference_two, 2)) + " percentage points away from the mean.")

# Print how far the third grade is from the mean, rounded to 2 decimal places
print("The third student is " + str(round(difference_three, 2)) + " percentage points away from the mean.")

# Print how far the fourth grade is from the mean, rounded to 2 decimal places
print("The fourth student is " + str(round(difference_four, 2)) + " percentage points away from the mean.")

# Print how far the fifth grade is from the mean, rounded to 2 decimal places
print("The fifth student is " + str(round(difference_five, 2)) + " percentage points away from the mean.")
