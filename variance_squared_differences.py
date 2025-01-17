# Importing the numpy library to handle numerical calculations
import numpy as np

# Define a list of grades (our dataset)
grades = [88, 82, 85, 84, 90]

# Calculate the mean (average) of the grades using numpy's mean function
mean = np.mean(grades)

# Calculate the squared differences between each grade and the mean
difference_one = (88 - mean) ** 2  # Square the difference for the first grade
difference_two = (82 - mean) ** 2  # Square the difference for the second grade
difference_three = (85 - mean) ** 2  # Square the difference for the third grade
difference_four = (84 - mean) ** 2  # Square the difference for the fourth grade
difference_five = (90 - mean) ** 2  # Square the difference for the fifth grade

# Part 1: Sum of the squared differences
# Add all the squared differences together
difference_sum = (difference_one +
                  difference_two +
                  difference_three +
                  difference_four +
                  difference_five)

# Part 2: Variance calculation
# Divide the sum of squared differences by the number of data points (5)
variance = difference_sum / 5

# Print the sum of the squared differences
print("The sum of the squared differences is " + str(difference_sum))

# Print the variance of the dataset
print("The variance is " + str(variance))
