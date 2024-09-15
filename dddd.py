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

# Graficar la función identidad y = x y el círculo bajo la transformación
def graficar_identidad_y_circulo():
    # Grilla para las coordenadas elípticas
    mu_vals = np.linspace(0.1, 2, 100)
    nu_vals = np.linspace(0, 2 * np.pi, 100)

    plt.figure(figsize=(6, 6))

    # Graficar la función identidad y = x en coordenadas cartesianas
    x_vals = np.linspace(0, 2 * np.pi, 100)
    y_vals = x_vals
    plt.plot(x_vals, y_vals, 'g--', label='Identidad y = x (cartesiana)', lw=2)

    # Transformar la identidad bajo coordenadas elípticas
    mu_vals_identity = np.linspace(0.1, 2, 100)
    nu_vals_identity = np.linspace(0, 2 * np.pi, 100)
    X, Y = elipticas(mu_vals_identity, mu_vals_identity)  # Transforma identidad
    plt.plot(X, Y, 'b', label='Identidad y = x (elíptica)', lw=2)

    # Graficar el círculo original en coordenadas cartesianas
    theta = np.linspace(0, 2 * np.pi, 100)
    circle_x = 0.5 + 0.5 * np.cos(theta)
    circle_y = 0.5 + 0.5 * np.sin(theta)
    plt.plot(circle_x, circle_y, 'r--', label='Círculo original', lw=2)

    # Graficar el círculo bajo la transformación elíptica
    X_circle, Y_circle = elipticas(mu_vals, nu_vals)
    plt.plot(X_circle, Y_circle, 'm', label='Círculo (elíptica)', lw=2)

    plt.title('Transformación elíptica de y = x y círculo')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.axis('equal')
    plt.show()

# Llamar a la función para graficar
graficar_identidad_y_circulo()
