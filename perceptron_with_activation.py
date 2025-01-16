# File name: perceptron_with_activation.py

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
    
    # Method to apply an activation function to the weighted sum
    def activation(self, weighted_sum):
        if weighted_sum >= 0:  # If the weighted sum is 0 or positive
            return 1           # Return +1
        else:                  # Otherwise (weighted sum is negative)
            return -1          # Return -1

# Create an instance of the Perceptron class
cool_perceptron = Perceptron()

# Calculate and print the weighted sum for the inputs [24, 55]
print(cool_perceptron.weighted_sum([24, 55]))

# Calculate and print the result of the activation function for a weighted sum of 52
print(cool_perceptron.activation(52))
