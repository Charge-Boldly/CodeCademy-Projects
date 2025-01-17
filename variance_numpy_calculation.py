# Import necessary libraries
import numpy as np  # For numerical operations
import matplotlib.pyplot as plt  # For creating plots
import codecademylib3_seaborn  # Preconfigured environment for consistent plots

# Dataset for teacher one's grades
teacher_one_grades = [80.24, 81.15, 81.29, 82.12, 82.52, 82.54, 82.76, 
                      83.37, 83.42, 83.45, 83.47, 83.79, 83.91, 83.98, 
                      84.03, 84.69, 84.74, 84.89, 84.95, 84.95, 85.02, 
                      85.18, 85.53, 86.29, 86.83, 87.29, 87.47, 87.62, 
                      88.04, 88.5]

# Dataset for teacher two's grades
teacher_two_grades = [65.82, 70.77, 71.46, 73.63, 74.62, 76.53, 76.86, 
                      77.06, 78.46, 79.81, 80.64, 81.61, 81.84, 83.67, 
                      84.44, 84.73, 84.74, 85.15, 86.55, 88.06, 88.53, 
                      90.12, 91.27, 91.62, 92.86, 94.37, 95.64, 95.99, 
                      97.69, 104.4]

# Calculate the variance for teacher one's grades using NumPy's var() function
teacher_one_variance = np.var(teacher_one_grades)

# Calculate the variance for teacher two's grades using NumPy's var() function
teacher_two_variance = np.var(teacher_two_grades)

# Plot histograms of both datasets to visualize the distribution
plt.hist(teacher_one_grades, alpha=0.75, label="Teacher 1 Scores", bins=7)  # Teacher one's grades with slight transparency
plt.hist(teacher_two_grades, alpha=0.5, label="Teacher 2 Scores", bins=30)  # Teacher two's grades with more bins and transparency
plt.title("Student test grades in two different classes")  # Title of the histogram
plt.xlabel("Grades")  # Label for the x-axis
plt.legend()  # Display the legend to differentiate datasets
plt.show()  # Render the plot

# Print the mean of each dataset
print("The mean of the test scores in teacher one's class is " + str(np.mean(teacher_one_grades)))
print("The mean of the test scores in teacher two's class is " + str(np.mean(teacher_two_grades)))

# Print the variance of each dataset
print("The variance of the test scores in teacher one's class is " + str(teacher_one_variance))
print("The variance of the test scores in teacher two's class is " + str(teacher_two_variance))
