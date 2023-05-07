import numpy as np
from scipy import stats

# Generate some sample data
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 3, 4, 5, 6])

# Perform simple linear regression
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)

# Print the regression coefficients and R-squared value
print(f"Slope: {slope:.2f}")
print(f"Intercept: {intercept:.2f}")
print(f"R-squared: {r_value**2:.2f}")
