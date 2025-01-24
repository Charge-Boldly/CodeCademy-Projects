import codecademylib3  # Required for Codecademy interactive learning environment
import pandas as pd  # Import pandas for data manipulation

# Load the NYC Tree Census dataset
nyc_trees = pd.read_csv("./nyc_tree_census.csv")  # Reads the CSV file into a DataFrame

# Show the first few rows of the dataset
print(nyc_trees.head())  # Displays the first 5 rows of the DataFrame to get an overview of the data

# Identifying categorical variables
# Categorical variables are typically non-numeric columns that represent categories, such as 'status', 'health', 'spc_common', and 'neighborhood'.

categorical_vars = ["status", "health", "spc_common", "neighborhood"]  # List of categorical variables
print(categorical_vars)  # Print the list of categorical variables
