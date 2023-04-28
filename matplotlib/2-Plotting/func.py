import matplotlib.pyplot as plt,numpy as np
# Define the function
f = lambda x: 2*x + 5

# Define a range of x values
x = range(-10, 11)

# Evaluate the function for each value of x
y = [f(i) for i in x]

# Plot the function
plt.plot(x, y)

# Add labels to the axes
plt.xlabel('x')
plt.ylabel('2x + 5')

# Display the plot
plt.show()

x = np.linspace(0, 10, 1000)
plt.plot(x,np.sin(x))
plt.show()