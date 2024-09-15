import numpy as np
import matplotlib.pyplot as plt

# Parámetros para la elipse
a = 1
b = 1

# Definir rangos para las coordenadas elípticas
mu = np.linspace(0, 2, 100)
nu = np.linspace(0, 2 * np.pi, 100)

# Crear una malla para las coordenadas elípticas
MU, NU = np.meshgrid(mu, nu)

# Convertir coordenadas elípticas a coordenadas cartesianas
X = a * np.cosh(MU) * np.cos(NU)
Y = b * np.sinh(MU) * np.sin(NU)

# Coloca la función que deseas graficar aquí
function1 = X - Y
function2 = ((X - (1/2)) + ((Y - (1/2))**2))/4

# Crear la gráfica 1
plt.figure(figsize=(8, 8))
plt.contour(X, Y, function1, levels=20, cmap='viridis')
plt.title("Gráfico de Coordenadas Elípticas")
plt.colorbar(label="Valor de la Función")
plt.show()

# Crear la gráfica 2
plt.figure(figsize=(8, 8))
plt.contour(X, Y, function2, levels=20, cmap='viridis')
plt.title("Gráfico de Coordenadas Elípticas")
plt.colorbar(label="Valor de la Función")
plt.show()
