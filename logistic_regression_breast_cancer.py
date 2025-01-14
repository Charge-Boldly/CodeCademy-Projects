# Filename: logistic_regression_breast_cancer.py

# Importing necessary libraries
import pandas as pd  # For data manipulation and analysis
import numpy as np  # For numerical computations
import codecademylib3  # Codecademy's library for resource management
import matplotlib.pyplot as plt  # For data visualization
import seaborn as sns  # For creating attractive statistical plots

# Importing machine learning modules from scikit-learn
from sklearn.model_selection import train_test_split  # For splitting data into training and testing sets
from sklearn.linear_model import LogisticRegression  # For implementing logistic regression
from sklearn.metrics import (  # For evaluating model performance
    confusion_matrix, classification_report, accuracy_score,
    precision_score, recall_score, f1_score
)

# Load the breast cancer dataset
df = pd.read_csv('breast_cancer_data.csv')  # Read data from a CSV file into a DataFrame

# Encode the diagnosis column: malignant (M) as 1, benign (B) as 0
df['diagnosis'] = df['diagnosis'].replace({'M': 1, 'B': 0})

# Define predictor variables (features) and the outcome variable (target)
predictor_var = ['radius_mean', 'texture_mean', 'compactness_mean', 'symmetry_mean']
outcome_var = 'diagnosis'

# Split the data into training and testing sets (70% training, 30% testing)
x_train, x_test, y_train, y_test = train_test_split(
    df[predictor_var], df[outcome_var], random_state=0, test_size=0.3
)

# Step 1: Define a logistic regression model with specific hyperparameters
log_reg = LogisticRegression(penalty='none', fit_intercept=True)  # No regularization, include intercept
print("Model Hyperparameters:", log_reg.get_params())  # Display the hyperparameters

# Step 2: Fit the model to the training data
log_reg.fit(x_train, y_train)  # Train the model
coefficients = log_reg.coef_  # Extract the model coefficients (weights for each feature)
intercept = log_reg.intercept_  # Extract the intercept term
print("Coefficients:", coefficients)  # Display the coefficients
print("Intercept:", intercept)  # Display the intercept

# Step 3: Evaluate the model using various metrics
y_pred = log_reg.predict(x_test)  # Predict the target variable for the test set

# Calculate performance metrics
accuracy = accuracy_score(y_test, y_pred)  # Proportion of correct predictions
precision = precision_score(y_test, y_pred)  # Proportion of true positives among predicted positives
recall = recall_score(y_test, y_pred)  # Proportion of true positives among actual positives
f1 = f1_score(y_test, y_pred)  # Harmonic mean of precision and recall

# Print the evaluation metrics
print(f"Test set accuracy:\t{accuracy}")
print(f"Test set precision:\t{precision}")
print(f"Test set recall:\t{recall}")
print(f"Test set f1-score:\t{f1}")

# Step 4: Print the confusion matrix
test_conf_matrix = pd.DataFrame(
    confusion_matrix(y_test, y_pred),  # Create the confusion matrix
    index=['actual no', 'actual yes'],  # Row labels for actual outcomes
    columns=['predicted no', 'predicted yes']  # Column labels for predicted outcomes
)
print("Confusion Matrix:")
print(test_conf_matrix)
