import pandas as pd  # Import pandas for data manipulation

# Read NYC Trees Data
nyc_trees = pd.read_csv("./nyc_tree_census.csv")  # Load the NYC Tree Census dataset into a pandas DataFrame

# Get tree counts by neighborhood
tree_counts = nyc_trees['neighborhood'].value_counts()  # Count the number of trees in each neighborhood
print(tree_counts)  # Print the count of trees in each neighborhood

# Get neighborhood with the most trees
greenest_neighborhood = tree_counts.index[0]  # The neighborhood with the most trees is the first item in the index
print(greenest_neighborhood)  # Print the name of the neighborhood with the most trees
