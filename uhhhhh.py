import numpy as np
import matplotlib.pyplot as plt

# Definir parámetros de la elipse
a = 5  # semi-eje mayor
b = 3  # semi-eje menor

# Crear una malla de coordenadas elípticas
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(-2, 2, 100)
U, V = np.meshgrid(u, v)

# Convertir coordenadas elípticas a coordenadas cartesianas
X = a * np.cos(U) * np.cosh(V)
Y = b * np.sin(U) * np.sinh(V)

# Graficar la función
plt.figure(figsize=(10, 7))
plt.contourf(X, Y, np.sin(X) + np.cos(Y), cmap='viridis')
plt.colorbar()
plt.title('Gráfico de la función en coordenadas elípticas')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
