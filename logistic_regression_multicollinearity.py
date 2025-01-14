# File Name: logistic_regression_multicollinearity.py

# Importing required libraries
import pandas as pd  # For data manipulation and analysis
import numpy as np  # For numerical operations
import matplotlib.pyplot as plt  # For creating visualizations
import seaborn as sns  # For advanced visualization, especially with statistical plots

# Importing machine learning tools from scikit-learn
from sklearn.model_selection import train_test_split  # To split the dataset into training and testing sets
from sklearn.linear_model import LogisticRegression  # For logistic regression modeling
from sklearn.metrics import (confusion_matrix, classification_report, accuracy_score, 
                              precision_score, recall_score, f1_score)  # For model evaluation

# Load the dataset
# The dataset is related to breast cancer diagnosis
df = pd.read_csv('breast_cancer_data.csv')

# Encode the diagnosis column
# 'M' (malignant) is encoded as 1, and 'B' (benign) is encoded as 0 for binary classification
df['diagnosis'] = df['diagnosis'].replace({'M': 1, 'B': 0})

# Define the predictor variables
# These are the columns we use to predict the diagnosis
predictor_var = ['radius_mean', 'texture_mean', 'perimeter_mean', 
                 'area_mean', 'smoothness_mean', 'compactness_mean', 
                 'concavity_mean', 'symmetry_mean', 'fractal_dimension_mean']

# Create a DataFrame 'x' with only the predictor variables
x = df[predictor_var]

# Plot logistic regression for the feature 'radius_mean'
# This visualizes how well 'radius_mean' predicts the diagnosis
sns.regplot(x='radius_mean', y='diagnosis', data=df, logistic=True)
plt.title('Logistic Regression: Radius Mean vs Diagnosis')
plt.show()
plt.close()

# Plot logistic regression for the feature 'fractal_dimension_mean'
# This visualizes how well 'fractal_dimension_mean' predicts the diagnosis
sns.regplot(x='fractal_dimension_mean', y='diagnosis', data=df, logistic=True)
plt.title('Logistic Regression: Fractal Dimension Mean vs Diagnosis')
plt.show()
plt.close()

# Plot a heatmap to identify multicollinearity
# This shows the correlation between all predictor variables
plt.figure(figsize=(10, 7))  # Set the figure size
sns.heatmap(x.corr(), annot=True, cmap='coolwarm')  # Display correlations with color and annotations
plt.title('Correlation Heatmap of Features')  # Title of the heatmap
plt.show()

# Define the correlated pair
# Exclude 'radius_mean', 'perimeter_mean', and 'area_mean' based on their high correlations
correlated_pair = ['compactness_mean', 'concavity_mean']  # Replace with actual pair from heatmap
print(f"Other correlated pair: {correlated_pair}")  # Display the identified correlated features
