import numpy as np
import matplotlib.pyplot as plt

# Parámetro de escala
a = 1

# Función de transformación elíptica
def elipticas(mu, nu, a=1):
    x = a * np.cosh(mu) * np.cos(nu)
    y = a * np.sinh(mu) * np.sin(nu)
    return x, y

# Graficar la función identidad y=x y el círculo en coordenadas elípticas
def graficar_transformadas():
    # Identidad y = x para x en [0, 2*pi]
    x_identidad = np.linspace(0, 2 * np.pi, 100)
    y_identidad = x_identidad
    
    # Círculo (x - 1/2)^2 + (y - 1/2)^2 = 1/4
    t = np.linspace(0, 2 * np.pi, 100)
    x_circulo = 0.5 + 0.5 * np.cos(t)
    y_circulo = 0.5 + 0.5 * np.sin(t)
    
    # Graficar en coordenadas cartesianas
    plt.figure(figsize=(10, 10))
    plt.subplot(1, 2, 1)
    plt.plot(x_identidad, y_identidad, label="y = x")
    plt.plot(x_circulo, y_circulo, label="Círculo", color='r')
    plt.title("Coordenadas Cartesianas")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.axis('equal')
    plt.grid(True)
    plt.legend()
    
    # Transformar a coordenadas elípticas
    # Asumimos que usamos mu y nu relacionados con x e y cartesianos, lo que requiere experimentación.
    # Aquí, para simplificación, lo aproximamos directamente con la transformación:
    
    mu_vals = np.linspace(0.1, 2, 100)  # Evitamos mu = 0 para evitar singularidad en cosh
    nu_vals_identidad = np.linspace(0, 2 * np.pi, 100)
    X_id, Y_id = elipticas(mu_vals, nu_vals_identidad)
    
    X_circulo, Y_circulo = elipticas(np.log(np.sqrt(x_circulo**2 + y_circulo**2)), np.arctan2(y_circulo, x_circulo))
    
    # Graficar en coordenadas elípticas
    plt.subplot(1, 2, 2)
    plt.plot(X_id, Y_id, label="Transformación de y = x")
    plt.plot(X_circulo, Y_circulo, label="Transformación del círculo", color='r')
    plt.title("Transformación Elíptica")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.axis('equal')
    plt.grid(True)
    plt.legend()

    plt.show()

# Llamada para graficar
graficar_transformadas()
