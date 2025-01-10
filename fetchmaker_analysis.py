# Filename: fetchmaker_analysis.py

# Import necessary libraries
import numpy as np  # For numerical operations
import pandas as pd  # For data manipulation and analysis
from scipy.stats import binom_test, f_oneway, chi2_contingency  # For hypothesis testing
from statsmodels.stats.multicomp import pairwise_tukeyhsd  # For Tukey's range test

# Load the dataset into a pandas DataFrame
# Assuming 'dog_data.csv' is in the same directory as this script
dogs = pd.read_csv('dog_data.csv')

# 1. Inspect the first 5 rows of the dataset
# This helps us understand the structure and content of the dataset
print(dogs.head())

# 2. Check if whippets are more or less likely to be rescues
# Filter rescue status (is_rescue) for only whippets
whippet_rescue = dogs.is_rescue[dogs.breed == 'whippet']

# 3. Count how many whippets are rescues
# We sum up the '1's in whippet_rescue to find rescued whippets
num_whippet_rescues = np.sum(whippet_rescue == 1)
print("Number of whippet rescues:", num_whippet_rescues)

# 4. Total number of whippets in the dataset
# Simply count the length of whippet_rescue
num_whippets = len(whippet_rescue)
print("Total number of whippets:", num_whippets)

# 5. Perform a binomial test
# Testing if 8% of whippets are rescues (null hypothesis)
pval_rescue = binom_test(x=num_whippet_rescues, n=num_whippets, p=0.08)
print("P-value for whippet rescue test:", pval_rescue)

# 6. Analyze average weights of whippets, terriers, and pitbulls
# Create separate series for each breed's weight
wt_whippets = dogs.weight[dogs.breed == 'whippet']
wt_terriers = dogs.weight[dogs.breed == 'terrier']
wt_pitbulls = dogs.weight[dogs.breed == 'pitbull']

# 7. Perform ANOVA test
# Compare weights across the three breeds
Fstat, pval_weights = f_oneway(wt_whippets, wt_terriers, wt_pitbulls)
print("P-value for weight ANOVA test:", pval_weights)

# 8. Tukey's range test to identify specific differences
# Subset data to only whippets, terriers, and pitbulls
dogs_wtp = dogs[dogs.breed.isin(['whippet', 'terrier', 'pitbull'])]

# Run Tukey's range test on the subset
results = pairwise_tukeyhsd(endog=dogs_wtp.weight, groups=dogs_wtp.breed)
print("Tukey's test results:\n", results)

# 9. Check color distributions of poodles and shihtzus
# Subset data to only poodles and shihtzus
dogs_ps = dogs[dogs.breed.isin(['poodle', 'shihtzu'])]

# Create a contingency table for color by breed
Xtab = pd.crosstab(dogs_ps.color, dogs_ps.breed)
print("Contingency table:\n", Xtab)

# 10. Perform Chi-Square test
# Test if color distribution is associated with breed
chi2, pval_color, dof, exp = chi2_contingency(Xtab)
print("P-value for color Chi-Square test:", pval_color)

# 11. Extra: Visualize the data for better insights
import matplotlib.pyplot as plt
import seaborn as sns

# Boxplot for weights of whippets, terriers, and pitbulls
sns.boxplot(x=dogs_wtp.breed, y=dogs_wtp.weight)
plt.title("Weight Distribution by Breed")
plt.xlabel("Breed")
plt.ylabel("Weight (lbs)")
plt.show()
