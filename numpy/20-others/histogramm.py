import numpy as np

# create a list of data
data = [1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 5]

# compute the histogram
hist, edges = np.histogram(data)

# print the histogram values and bin edges
print("Histogram values:", hist)
print("Bin edges:", edges)

from matplotlib import pyplot as plt
plt.hist(data, bins=50, color='magenta')
plt.title("Histogram of data")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.show()

plt.hist(hist,bins=edges)
plt.show()