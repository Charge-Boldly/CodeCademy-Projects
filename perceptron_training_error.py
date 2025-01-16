# File name: perceptron_training_error.py

class Perceptron:
    # Initialize the Perceptron class with default values for inputs and weights
    def __init__(self, num_inputs=2, weights=[1, 1]):
        self.num_inputs = num_inputs  # Store the number of inputs
        self.weights = weights        # Store the list of weights
    
    # Method to calculate the weighted sum of inputs
    def weighted_sum(self, inputs):
        weighted_sum = 0  # Start with a weighted sum of 0
        for i in range(self.num_inputs):  # Loop through each input
            weighted_sum += self.weights[i] * inputs[i]  # Multiply input by its weight and add to the sum
        return weighted_sum  # Return the final weighted sum
    
    # Method to apply the activation function (sign function) to the weighted sum
    def activation(self, weighted_sum):
        if weighted_sum >= 0:  # If the weighted sum is 0 or positive
            return 1           # Return +1
        if weighted_sum < 0:   # If the weighted sum is negative
            return -1          # Return -1

    # Method to train the perceptron by calculating training error
    def training(self, training_set):
        for inputs, actual in training_set:  # Unpack each element as inputs and actual
            # Calculate the perceptron's prediction using weighted_sum and activation
            prediction = self.activation(self.weighted_sum(inputs))
            # Calculate the training error as the difference between actual and predicted
            error = actual - prediction
            # Print the details for each training example
            print(f"Inputs: {inputs}, Actual: {actual}, Prediction: {prediction}, Error: {error}")

# Create an instance of the Perceptron class
cool_perceptron = Perceptron()

# Print the weighted sum for the inputs [24, 55]
print(cool_perceptron.weighted_sum([24, 55]))

# Print the result of the activation function for a weighted sum of 52
print(cool_perceptron.activation(52))

# Define a training set where each element is a tuple of (inputs, actual label)
training_set = [
    ([2, 3], 1),  # Inputs: [2, 3], Actual label: 1
    ([-1, -1], -1),  # Inputs: [-1, -1], Actual label: -1
    ([4, -2], 1),  # Inputs: [4, -2], Actual label: 1
    ([-2, 4], -1)  # Inputs: [-2, 4], Actual label: -1
]

# Train the perceptron using the training set
cool_perceptron.training(training_set)
