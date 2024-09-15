import numpy as np
import matplotlib.pyplot as plt

# Parameters for the ellipse
a = 2
b = 1

# Define ranges for elliptic coordinates
mu = np.linspace(0, 2, 100)
nu = np.linspace(0, 2 * np.pi, 100)

# Create a meshgrid for elliptic coordinates
MU, NU = np.meshgrid(mu, nu)

# Convert elliptic coordinates to Cartesian coordinates
X = a * np.cosh(MU) * np.cos(NU)
Y = b * np.sinh(MU) * np.sin(NU)

# Create the plot
plt.figure(figsize=(8, 8))
plt.contour(X, Y, X**2 + Y**2, levels=20, cmap='viridis')
plt.title("Elliptic Coordinates Plot")
plt.xlabel("x")
plt.ylabel("y")
plt.colorbar(label="Function Value")
plt.show()
