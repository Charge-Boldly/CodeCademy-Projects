# Import libraries
import pandas as pd
import numpy as np
from scipy.stats import ttest_1samp, ttest_ind, chi2_contingency

# Load datasets
lifespans = pd.read_csv('familiar_lifespan.csv')
iron = pd.read_csv('familiar_iron.csv')

# Task 1: Inspect the lifespans dataset
print("Lifespans dataset:")
print(lifespans.head())

# Task 2: Extract lifespans for Vein Pack subscribers
vein_pack_lifespans = lifespans.lifespan[lifespans.pack == 'vein']

# Task 3: Calculate mean lifespan for Vein Pack subscribers
vein_pack_mean = np.mean(vein_pack_lifespans)
print("\nMean lifespan for Vein Pack subscribers:", vein_pack_mean)

# Task 4 & 5: Perform a one-sample t-test
t_stat, p_value = ttest_1samp(vein_pack_lifespans, 73)
print("\nOne-sample t-test results: p-value =", p_value)

# Task 6: Extract lifespans for Artery Pack subscribers
artery_pack_lifespans = lifespans.lifespan[lifespans.pack == 'artery']

# Task 7: Calculate mean lifespan for Artery Pack subscribers
artery_pack_mean = np.mean(artery_pack_lifespans)
print("\nMean lifespan for Artery Pack subscribers:", artery_pack_mean)

# Task 8 & 9: Perform a two-sample t-test
t_stat, p_value = ttest_ind(vein_pack_lifespans, artery_pack_lifespans)
print("\nTwo-sample t-test results: p-value =", p_value)

# Task 10: Inspect the iron dataset
print("\nIron dataset:")
print(iron.head())

# Task 11: Create a contingency table for iron levels and packs
Xtab = pd.crosstab(iron.pack, iron.iron)
print("\nContingency table:")
print(Xtab)

# Task 12 & 13: Perform a chi-square test for association
chi2, p_value, dof, expected = chi2_contingency(Xtab)
print("\nChi-square test results: p-value =", p_value)
