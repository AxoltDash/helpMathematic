import numpy as np
import matplotlib.pyplot as plt

# Elliptic coordinate transformation functions
def elliptic_to_cartesian(sigma, tau, a=1):
    x = a * np.cosh(sigma) * np.cos(tau)
    y = a * np.sinh(sigma) * np.sin(tau)
    return x, y

# Define elliptic coordinates ranges
sigma = np.linspace(0, 2, 100)   # Range for sigma
tau = np.linspace(0, 2 * np.pi, 100)  # Range for tau

# Create a meshgrid for elliptic coordinates
Sigma, Tau = np.meshgrid(sigma, tau)

# Define the function to plot
r = np.sin(Sigma)  # Example function

# Convert elliptic coordinates to Cartesian
X, Y = elliptic_to_cartesian(Sigma, Tau)

# Create the plot
plt.figure(figsize=(8, 8))
plt.contourf(X, Y, r, cmap='viridis')  # Plot the function as a filled contour
plt.colorbar()  # Show color scale
plt.title('Plot of the function in Elliptic Coordinates')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
