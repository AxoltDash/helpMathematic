import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Parámetro de escala
a = 1

# Función de transformación elíptica
def elipticas(mu, nu, a=1):
    x = a * np.cosh(mu) * np.cos(nu)
    y = a * np.sinh(mu) * np.sin(nu)
    return x, y

# Graficar cuadrícula cartesiana transformada
mu_vals = np.linspace(0.1, 2, 10)  # Evitamos mu = 0 para evitar singularidad en cosh
nu_vals = np.linspace(0, 2*np.pi, 100)

plt.figure(figsize=(6,6))

# Graficar líneas de la cuadrícula elíptica
for mu in mu_vals:
    X, Y = elipticas(mu, nu_vals)
    plt.plot(X, Y, 'b', lw=1)  # Líneas azules para la cuadrícula

for nu in np.linspace(0, 2*np.pi, 10):
    mu_vals = np.linspace(0.1, 2, 100)
    X, Y = elipticas(mu_vals, nu)
    plt.plot(X, Y, 'r', lw=1)  # Líneas rojas para la cuadrícula

plt.title("Cuadrícula cartesiana transformada a coordenadas elípticas")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.axis('equal')
plt.show()

# Cálculo del factor de cambio de área (Jacobiano)
mu, nu = sp.symbols('mu nu')
x = a * sp.cosh(mu) * sp.cos(nu)
y = a * sp.sinh(mu) * sp.sin(nu)

# Derivadas parciales para el Jacobiano
J = sp.Matrix([[sp.diff(x, mu), sp.diff(x, nu)],
               [sp.diff(y, mu), sp.diff(y, nu)]])

# Determinante del Jacobiano
det_J = J.det()
det_J_simplified = sp.simplify(det_J)
print("Factor de cambio de área (determinante del Jacobiano):")
sp.pprint(det_J_simplified)
