import numpy as np
from scipy.stats import ttest_ind

#normal distribtion with equal variance
v1 = np.random.normal(size=100)
v2 = np.random.normal(size=100)

res = ttest_ind(v1, v2)

# Get the p-value from the test result
p_value = res.pvalue

# Print the p-value
print("The p-value is:", p_value)

# Check if the p-value is less than the significance level (e.g. 0.05)
if p_value < 0.05:
    print("The null hypothesis (the two distributions have identica average) can be rejected.")
    print("There is significant evidence to suggest that the two populations don't have identical average.")
else:
    print("There is not enough evidence to suggest that the two populations have identical average.")

print(np.mean(v1))
print(np.mean(v2))
