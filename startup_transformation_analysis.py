# Import necessary libraries
import codecademylib3
from sklearn import preprocessing
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

# Task 1: Load and inspect the financial data
financial_data = pd.read_csv('financial_data.csv')
print(financial_data.head())

# Task 2: Extract columns
month = financial_data['Month']
revenue = financial_data['Revenue']
expenses = financial_data['Expenses']

# Task 3: Plot revenue over time
plt.plot(month, revenue)
plt.xlabel('Month')
plt.ylabel('Amount ($)')
plt.title('Revenue')
plt.show()

# Task 5: Plot expenses over time
plt.clf()
plt.plot(month, expenses)
plt.xlabel('Month')
plt.ylabel('Amount ($)')
plt.title('Expenses')
plt.show()

# Task 6: Load and inspect the expense data
expense_overview = pd.read_csv('expenses.csv')
print(expense_overview.head(7))

# Task 7: Extract columns for the pie chart
expense_categories = expense_overview['Expense']
proportions = expense_overview['Proportion']

# Task 8: Create a pie chart
plt.clf()
plt.pie(proportions, labels=expense_categories, autopct='%1.1f%%')
plt.title('Expense Breakdown')
plt.axis('Equal')
plt.tight_layout()
plt.show()

# Task 10: Collapse small expense categories into 'Other'
expense_overview['Proportion'] = expense_overview['Proportion'].apply(lambda x: x if x >= 0.05 else 0)
expense_overview.loc[len(expense_overview)] = ['Other', 1 - sum(expense_overview['Proportion'])]
proportions = expense_overview['Proportion']
expense_categories = expense_overview['Expense']

# Updated pie chart
plt.clf()
plt.pie(proportions, labels=expense_categories, autopct='%1.1f%%')
plt.title('Simplified Expense Breakdown')
plt.axis('Equal')
plt.tight_layout()
plt.show()

# Task 11: Expense cut category
expense_cut = 'Salaries'

# Task 12: Load and inspect employee data
employees = pd.read_csv('employees.csv')
print(employees.head())

# Task 13: Sort employees by productivity
sorted_productivity = employees.sort_values(by=['Productivity'])
print(sorted_productivity)

# Task 14: Select the least productive 100 employees
employees_cut = sorted_productivity.head(100)
print(employees_cut)

# Task 15: Transformation recommendation
transformation = 'Standardization'

# Task 16: Analyze commute times
commute_times = employees['Commute Time']
print(commute_times.describe())

# Task 18: Histogram of commute times
plt.clf()
plt.hist(commute_times, bins=10, edgecolor='black')
plt.xlabel('Commute Time (minutes)')
plt.ylabel('Frequency')
plt.title('Commute Time Distribution')
plt.show()

# Task 19: Log transformation
commute_times_log = np.log(commute_times + 1)

# Task 20: Histogram of log-transformed commute times
plt.clf()
plt.hist(commute_times_log, bins=10, edgecolor='black')
plt.xlabel('Log(Commute Time + 1)')
plt.ylabel('Frequency')
plt.title('Log-Transformed Commute Time Distribution')
plt.show()
