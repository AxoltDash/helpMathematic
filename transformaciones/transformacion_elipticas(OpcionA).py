import numpy as np
import matplotlib.pyplot as plt

# Define the elliptic coordinate function
def elliptic_coordinates(mu, nu):
    x = np.cosh(mu) * np.cos(nu)
    y = np.sinh(mu) * np.sin(nu)
    return x, y

# Define the function to plot
def function_swap(mu, nu, flag):
    x, y = elliptic_coordinates(mu, nu)
    if flag == 1:
        return x - y
    else:
        return (((x - (1/2)) + (y - ((1/2))**2))*4) -1
# Define ranges for mu and nu
mu_range = np.linspace(0, 2, 100)  # Range of mu from 0 to 2
nu_range = np.linspace(0, 2 * np.pi, 100)  # Range of nu from 0 to 2*pi

# Create a meshgrid for mu and nu
mu, nu = np.meshgrid(mu_range, nu_range)

# Compute the function values
values1 = function_swap(mu, nu, 1)
values2 = function_swap(mu, nu, 2)

# Plot the result 1
plt.figure(figsize=(10, 6))
plt.contourf(nu, mu, values1, levels=np.linspace(-1, 1, 100), cmap='viridis')
plt.colorbar(label='Function Value')
plt.title('Elliptic Coordinates x = y')
plt.xlabel('nu')
plt.ylabel('mu')
plt.contour(nu, mu, values1, levels=[0], colors='red')  # Plot function as a red line
plt.show()

# Plot the result 2
plt.figure(figsize=(10, 6))
plt.contourf(nu, mu, values2, levels=np.linspace(-1, 1, 100), cmap='viridis')
plt.colorbar(label='Function Value')
plt.title('Elliptic Coordinates (x - (1/2) + (y - (1/2)^2 = 1/4')
plt.xlabel('nu')
plt.ylabel('mu')
plt.contour(nu, mu, values2, levels=[0], colors='red')  # Plot function as a red line
plt.show()