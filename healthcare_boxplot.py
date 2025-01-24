# Import necessary libraries
import codecademylib3_seaborn  # Required to run the Codecademy interactive environment
import pandas as pd  # Used for data manipulation and analysis
from matplotlib import pyplot as plt  # Used for creating visual plots like boxplots

# Load the dataset into a variable named 'healthcare'
healthcare = pd.read_csv("healthcare.csv")  # Reads the CSV file 'healthcare.csv' into a DataFrame

# Investigate the first few rows of the data
print(healthcare.head())  # Displays the first five rows of the dataset to get an overview

# Check all unique diagnoses in the dataset to find the chest pain diagnosis
print(healthcare["DRG Definition"].unique())  # Prints all unique diagnoses available in the dataset

# Filter data for chest pain diagnosis ('313 - CHEST PAIN')
chest_pain = healthcare[healthcare['DRG Definition'] == '313 - CHEST PAIN']  # Keeps only the rows related to chest pain

# Separate data by state (example for Alabama)
alabama_chest_pain = chest_pain[chest_pain['Provider State'] == "AL"]  # Filters rows for Alabama (AL)

# Extract the 'Average Covered Charges' column for Alabama chest pain data
costs = alabama_chest_pain[' Average Covered Charges '].values  # Gets the costs as a NumPy array from the filtered data

# Create a boxplot for Alabama chest pain charges
plt.boxplot(costs)  # Plots a boxplot of the costs for chest pain in Alabama
plt.show()  # Displays the plot

# Get a list of all unique states
states = chest_pain['Provider State'].unique()  # Creates a list of unique state abbreviations from the 'Provider State' column

# Create an empty list to store datasets for each state
datasets = []  # This list will hold the costs for each state

# Loop through each state and create a dataset of 'Average Covered Charges' for chest pain in that state
for state in states:  # Loops through each state in the 'states' list
    state_data = chest_pain[chest_pain['Provider State'] == state]  # Filters chest pain data for the current state
    state_costs = state_data[' Average Covered Charges '].values  # Gets the costs for that s
