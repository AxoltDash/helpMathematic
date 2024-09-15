import numpy as np
import matplotlib.pyplot as plt

# Parameters for the ellipse
a = 2
b = 1

# Define ranges for elliptic coordinates
mu = np.linspace(0, 2, 100)
nu = np.linspace(0, 2 * np.pi, 100)

# Create meshgrid for elliptic coordinates
MU, NU = np.meshgrid(mu, nu)

# Compute the Cartesian coordinates
X = a * np.cosh(MU) * np.cos(NU)
Y = b * np.sinh(MU) * np.sin(NU)

# Compute the line x = y in elliptic coordinates
coth_mu = (b * np.sin(NU)) / (a * np.cos(NU))
MU_line = np.arctanh(coth_mu)

# Compute Cartesian coordinates for the line
X_line = a * np.cosh(MU_line) * np.cos(NU)
Y_line = b * np.sinh(MU_line) * np.sin(NU)

# Create the plot
plt.figure(figsize=(8, 8))
plt.contour(X, Y, X**2 + Y**2, levels=20, cmap='viridis')
plt.plot(X_line, Y_line, 'r--', label='$x = y$ in Elliptic Coordinates')
plt.title("Plot of x = y in Elliptic Coordinates")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.colorbar(label="Function Value")
plt.show()
    