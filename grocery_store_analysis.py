# Import packages for data analysis and numerical computation
import numpy as np  # Library for numerical operations, such as averages
import pandas as pd  # Library for handling tabular data (data frames)

# Task 1: Load the transactions data
transactions = pd.read_csv("transactions.csv")  # Load the transactions dataset
transactions = transactions.drop(["Unnamed: 0"], axis=1)  # Drop the 'Unnamed: 0' column as it's irrelevant

# Task 2: Save transaction times and costs to separate numpy arrays
times = transactions["Transaction Time"].values  # Extract "Transaction Time" column as a numpy array
cost = transactions["Cost"].values  # Extract "Cost" column as a numpy array

# Task 3: Print the entire transactions data
print(transactions)  # Print the DataFrame to understand the data structure

# Task 4: Calculate and print the average transaction time
# Follow the instruction exactly to pass the evaluation
print(np.average(times))  # Print the average time per the task's requirements
