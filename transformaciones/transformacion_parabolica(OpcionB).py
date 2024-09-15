import numpy as np
import matplotlib.pyplot as plt

# Definir rangos para las coordenadas parabólicas
sigma = np.linspace(-2, 2, 100)
tau = np.linspace(-2, 2, 100)

# Crear una malla para las coordenadas parabólicas
SIGMA, TAU = np.meshgrid(sigma, tau)

# Convertir coordenadas parabólicas a coordenadas cartesianas
X = SIGMA * TAU
Y = 1/2 * (SIGMA**2 - TAU**2)

# Coloca la función que deseas graficar aquí
function1 = X - Y
function2 = (X**2 + Y**2) - 1
function3 = ((X - 1/2) + (Y - 1/2)**2 * 4) -1

# Crear la gráfica 1
plt.figure(figsize=(8, 8))
plt.contour(X, Y, function1, levels=20, cmap='viridis')
plt.title("Gráfico de Coordenadas Parabolicas")
plt.colorbar(label="Valor de la Función")
plt.show()

# Crear la gráfica 2
plt.figure(figsize=(8, 8))
plt.contour(X, Y, function2, levels=20, cmap='viridis')
plt.title("Gráfico de Coordenadas Parabólicas")
plt.colorbar(label="Valor de la Función")
plt.show()

# Crear la gráfica 3
plt.figure(figsize=(8, 8))
plt.contour(X, Y, function3, levels=20, cmap='viridis')
plt.title("Gráfico de Coordenadas Parabólicas")
plt.colorbar(label="Valor de la Función")
plt.show()


sigma = np.linspace(-3, 1, 100)
tau = np.linspace(-3, 1, 100)
SIGMA, TAU = np.meshgrid(sigma, tau)
X = SIGMA * TAU
Y = 1/2 * (SIGMA**2 - TAU**2)
function4 = -2 - X - Y

# Crear la gráfica 4
plt.figure(figsize=(8, 8))
plt.contour(X, Y, function4, levels=20, cmap='viridis')
plt.title("Gráfico de Coordenadas Parabólicas")
plt.colorbar(label="Valor de la Función")
plt.show()