# Importing the numpy library for numerical operations
import numpy as np

# Define a list of grades (our dataset)
grades = [88, 82, 85, 84, 90]

# Calculate the average (mean) of the grades using numpy's mean function
mean = np.mean(grades)

# Compute the differences between each grade and the mean
difference_one = 88 - mean  # Difference for the first grade
difference_two = 82 - mean  # Difference for the second grade
difference_three = 85 - mean  # Difference for the third grade
difference_four = 84 - mean  # Difference for the fourth grade
difference_five = 90 - mean  # Difference for the fifth grade

# Part 1: Sum the differences
# Add all the differences together
difference_sum = (difference_one +
                  difference_two +
                  difference_three +
                  difference_four +
                  difference_five)

# Part 2: Average the differences
# Divide the sum of differences by the number of grades
average_difference = difference_sum / 5

# IGNORE CODE BELOW HERE
# Print the sum of the differences, formatted as a float
print("The sum of the differences is " + str(format(difference_sum, "f")))

# Print the average of the differences, formatted as a float
print("The average difference is " + str(format(average_difference, "f")))
