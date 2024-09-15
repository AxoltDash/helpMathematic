import numpy as np
import matplotlib.pyplot as plt

# Parámetro de escala
a = 1

# Función de transformación elíptica
def elipticas(mu, nu, a=1):
    x = a * np.cosh(mu) * np.cos(nu)
    y = a * np.sinh(mu) * np.sin(nu)
    return x, y

# Función identidad y = x
def identidad(x):
    return x

# Función para el círculo (x - 1/2)^2 + (y - 1/2)^2 = 1/4
def circulo():
    theta = np.linspace(0, 2 * np.pi, 100)
    x = 0.5 + 0.5 * np.cos(theta)
    y = 0.5 + 0.5 * np.sin(theta)
    return x, y

# Graficar la función identidad y el círculo
def graficar_identidad_y_circulo():
    x_vals = np.linspace(0, 2*np.pi, 100)
    y_vals_identidad = identidad(x_vals)
    
    x_circulo, y_circulo = circulo()

    plt.figure(figsize=(6,6))
    
    # Graficar función identidad
    plt.plot(x_vals, y_vals_identidad, label="Identidad: y = x", color='green')

    # Graficar círculo
    plt.plot(x_circulo, y_circulo, label="Círculo: (x - 1/2)^2 + (y - 1/2)^2 = 1/4", color='blue')

    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Imagen identidad y círculo en coordenadas cartesianas")
    plt.legend()
    plt.axis('equal')
    plt.grid(True)
    plt.show()

# Graficar bajo transformación elíptica
def graficar_eliptica_transformada():
    x_vals = np.linspace(1, 2*np.pi, 100)  # Filtramos x >= 1 para que arccosh esté bien definida
    y_vals_identidad = identidad(x_vals)
    
    # Transformamos la función identidad
    mu_vals = np.arccosh(x_vals/a)
    nu_vals_identidad = np.linspace(0, 2*np.pi, 100)
    
    x_trans_identidad, y_trans_identidad = elipticas(mu_vals, nu_vals_identidad)
    
    # Transformamos el círculo
    x_circulo, y_circulo = circulo()
    x_circulo_validos = x_circulo[x_circulo >= 1]  # Filtramos los valores de x >= 1
    mu_vals_circulo = np.arccosh(x_circulo_validos/a)
    nu_vals_circulo = np.linspace(0, 2*np.pi, len(mu_vals_circulo))
    x_trans_circulo, y_trans_circulo = elipticas(mu_vals_circulo, nu_vals_circulo)
    
    plt.figure(figsize=(6,6))

    # Graficar identidad transformada
    plt.plot(x_trans_identidad, y_trans_identidad, label="Identidad transformada", color='red')

    # Graficar círculo transformado
    plt.plot(x_trans_circulo, y_trans_circulo, label="Círculo transformado", color='purple')

    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Identidad y círculo transformados bajo coordenadas elípticas")
    plt.legend()
    plt.axis('equal')
    plt.grid(True)
    plt.show()

# Ejecutamos las gráficas
graficar_identidad_y_circulo()
graficar_eliptica_transformada()
