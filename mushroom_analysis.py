import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Load the data
df = pd.read_csv("mushroom_data.csv")

# List of all column headers
columns = df.columns.tolist()

# Loop through each column in the dataset
for column in columns:
    # Create a countplot for each column
    sns.countplot(data=df, x=column, order=df[column].value_counts().index)
    
    # Set the title and axis labels for clarity
    plt.title(f"{column} Value Counts", fontsize=14)
    plt.xlabel(column, fontsize=12)
    plt.ylabel("Count", fontsize=12)
    
    # Adjust the x-axis for better readability
    plt.xticks(rotation=30, fontsize=10)
    
    # Show the plot and clear the figure for the next one
    plt.show()
    plt.clf()
