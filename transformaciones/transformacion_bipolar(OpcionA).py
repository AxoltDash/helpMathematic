import numpy as np
import matplotlib.pyplot as plt

# Aqui se hace el cambio de coordenadas bipolares a cartesianas g(sigma,teo) = (sinh(sigma)/cosh(tau) - cos(sigma), sinh(tau)/cosh(tau) - cos(sigma))
def coordenadas_bipolares(sigma, tau):
    x = np.sinh(sigma)/(np.cosh(tau) - np.cos(sigma))
    y = np.sinh(tau)/(np.cosh(tau) - np.cos(sigma))
    return x, y

# Aqui se define la función a graficar, el segun la "flag" que se le pase, se graficará una función diferente
def definir_funcion(sigma, tau, flag):
    x, y = coordenadas_bipolares(sigma, tau)
    if flag == 1:
        return x - y
    
    elif flag == 2:
        return x**2 + y**2 - 1
    
    else: #Si la flag es 3 u otra
        return -2-x-y

# Aqui se define la función para graficar
def graficar(values, Title):
    plt.figure(figsize=(10, 6))
    plt.contourf(sigma, tau, values, levels=np.linspace(-1, 1, 100), cmap='inferno')
    plt.colorbar(label='Function Value')
    plt.title('Coordenadas Bipolares: ' + Title)
    plt.xlabel('sigma')
    plt.ylabel('tau')
    plt.contour(sigma, tau, values, levels=[0], colors='cyan')  # Plot function as a red line
    plt.show()

# Aqui se definen los rangos para sigma y tau
sigma_range = np.linspace(-np.pi, np.pi/4, 100) #en [-pi, pi/4]
tau_range = np.linspace(-np.pi, np.pi/4, 100) #en [-pi, pi/4]

# Aqui se pasan a una malla (Esto ya es de programación en general)
sigma, tau = np.meshgrid(sigma_range, tau_range)

# Aqui asignamos las funciones a graficar
funcion1 = definir_funcion(sigma, tau, 1) # x = y
funcion2 = definir_funcion(sigma, tau, 2) # x^2 + y^2 = 1

# Se grafican (y se pone el texto que aparecerá en la gráfica)
graficar(funcion1,'x = y')
graficar(funcion2,'x^2 + y^2 = 1')

# Hacemo todo de nuevo para la 3 ya que nos cambian los rangos
sigma_range = np.linspace(-6, 4, 100) #en [-6, 4]
tau_range = np.linspace(-6, 4, 100)
sigma, tau = np.meshgrid(sigma_range, tau_range)
funcion3 = definir_funcion(sigma, tau, 3) # -2-x-y
graficar(funcion3,'y = -2-x')
