import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# 1. Definir el rango de valores de x
x_vals = np.linspace(0, 2 * np.pi, 400)

# 2. Función identidad y = x
y_vals = x_vals

# 3. Ecuación del círculo (x - 1/2)^2 + (y - 1/2)^2 = 1/4
# Resolver paramétricamente
theta = np.linspace(0, 2 * np.pi, 400)
r = 1/2
x_circle = r * np.cos(theta) + 1/2
y_circle = r * np.sin(theta) + 1/2

# 4. Definir la transformación a coordenadas elípticas
# Por ejemplo, una transformación sencilla podría ser:
# u = sqrt(x^2 + y^2)
# v = arctan(y / x)
def eliptic_transform(x, y):
    u = np.sqrt(x**2 + y**2)
    v = np.arctan2(y, x)
    return u, v

# Aplicar la transformación elíptica a los puntos de la identidad
u_vals, v_vals = eliptic_transform(x_vals, y_vals)

# Aplicar la transformación elíptica a los puntos del círculo
u_circle, v_circle = eliptic_transform(x_circle, y_circle)

# 5. Graficar los resultados
plt.figure(figsize=(10, 5))

# Graficar la identidad y=x antes y después de la transformación
plt.subplot(1, 2, 1)
plt.plot(x_vals, y_vals, label='Identidad: y=x')
plt.plot(x_circle, y_circle, label='Círculo original')
plt.title('Curvas Originales')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

# Graficar la transformación elíptica
plt.subplot(1, 2, 2)
plt.plot(u_vals, v_vals, label='Transformación elíptica (Identidad)')
plt.plot(u_circle, v_circle, label='Transformación elíptica (Círculo)')
plt.title('Curvas Transformadas a Coordenadas Elípticas')
plt.xlabel('u')
plt.ylabel('v')
plt.legend()

plt.tight_layout()
plt.show()
