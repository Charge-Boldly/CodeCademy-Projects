# Filename: perceptron_logic_gate.py
import codecademylib3_seaborn  # Importing the seaborn library for plotting
from sklearn.linear_model import Perceptron  # Importing the Perceptron class from scikit-learn
import matplotlib.pyplot as plt  # Importing matplotlib for plotting
import numpy as np  # Importing numpy for numerical operations
from itertools import product  # Importing product to create a grid of points

# 1. Creating the data representing the inputs for the AND gate
# Inputs to AND gate are: [0,0], [0,1], [1,0], [1,1]
data = [[0, 0], [0, 1], [1, 0], [1, 1]]  # Defining the data points for the AND gate

# 2. Labels for AND gate
# The output of the AND gate is: 0 for [0,0], 0 for [0,1], 0 for [1,0], 1 for [1,1]
labels = [0, 0, 0, 1]  # Defining the output labels for the corresponding inputs

# 3. Plotting the data points on a graph
# The x values are the first element in each data point, the y values are the second element
# 'c' parameter is used to color the points based on their labels (0 or 1)
plt.scatter([point[0] for point in data], [point[1] for point in data], c=labels)
plt.show()  # Display the plot

# 4. Creating the Perceptron model to learn the AND gate
# max_iter is the number of iterations the model will go through the training data
# random_state ensures reproducibility by setting a seed for random number generation
classifier = Perceptron(max_iter=40, random_state=22)  # Initializing the Perceptron

# 5. Training the Perceptron using the data and labels
classifier.fit(data, labels)  # Fitting the model on the data and labels

# 6. Checking the accuracy of the Perceptron
accuracy = classifier.score(data, labels)  # Checking the accuracy of the trained model
print(accuracy)  # Printing the accuracy

# 7. Changing the labels to represent an XOR gate
# XOR gate outputs 1 for [0,1], [1,0], and 0 for [0,0], [1,1]
labels = [0, 1, 1, 0]  # New labels for the XOR gate

# Training the model again with the new labels
classifier.fit(data, labels)

# Checking the accuracy again for XOR data
accuracy = classifier.score(data, labels)  # Checking the accuracy on XOR data
print(accuracy)  # Printing the accuracy

# 8. Changing the labels to represent an OR gate
# OR gate outputs 1 for [0,1], [1,0], [1,1] and 0 for [0,0]
labels = [0, 1, 1, 1]  # New labels for the OR gate

# Training the model again with OR labels
classifier.fit(data, labels)

# Checking the accuracy for OR data
accuracy = classifier.score(data, labels)  # Checking the accuracy on OR data
print(accuracy)  # Printing the accuracy

# 9. Visualizing the decision function of the perceptron
# decision_function gives the distance of each point from the decision boundary
# A positive value means it’s classified as 1, and a negative value means 0
print(classifier.decision_function([[0, 0], [1, 1], [0.5, 0.5]]))  # Testing the decision function

# 10. Creating a grid of points to visualize the decision boundary
# Generating 100 evenly spaced points between 0 and 1 for both x and y axes
x_values = np.linspace(0, 1, 100)
y_values = np.linspace(0, 1, 100)

# 11. Creating a grid of all combinations of x and y values
point_grid = list(product(x_values, y_values))  # Creating a grid of points from x_values and y_values

# 12. Getting the distances from the decision boundary for each point in the grid
distances = classifier.decision_function(point_grid)  # Getting decision function values for the grid

# 13. Taking the absolute value of each distance, since we care about the distance, not the sign
abs_distances = [abs(pt) for pt in distances]  # Getting the absolute value of the distances

# 14. Reshaping the distances into a 100x100 2D array to visualize it
distances_matrix = np.reshape(abs_distances, (100, 100))  # Reshaping the list into a 2D array

# 15. Plotting the heatmap of the decision boundary using pcolormesh
heatmap = plt.pcolormesh(x_values, y_values, distances_matrix)  # Creating the heatmap
plt.colorbar(heatmap)  # Adding a color bar to the heatmap
plt.show()  # Displaying the heatmap

# 16. Final steps to test the visualizations with different gates (OR, XOR)
# You can change the labels to represent an OR gate or XOR gate and visualize where the decision boundaries are
