import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la elipse
a = 2
b = 1

# Crear un rango de valores para u (ángulo elíptico)
u = np.linspace(0.1, 2 * np.pi, 400)

# Crear un rango de valores para v (parámetro elíptico)
v = np.linspace(-2, 2, 400)

# Crear una cuadrícula para u y v
U, V = np.meshgrid(u, v)

# Calcular x y y
X = a * np.cos(U) * np.cosh(V)
Y = b * np.sin(U) * np.sinh(V)

# Graficar
plt.figure(figsize=(10, 6))
plt.contourf(X, Y, U, levels=50, cmap='viridis')
plt.colorbar(label='u')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráfico de la función en coordenadas elípticas')
plt.show()
