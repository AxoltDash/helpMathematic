import numpy as np
import matplotlib.pyplot as plt

# Aqui se hace el cambio de coordenadas parabólicas a cartesianas g(sigma,teo) = (sigma*tau, 1/2(sigma^2 - tau^2))
def coordenadas_parabolicas(sigma, tau):
    x = sigma * tau
    y = 1/2 * (sigma**2 - tau**2)
    return x, y

# Aqui se define la función a graficar, el segun la "flag" que se le pase, se graficará una función diferente
def definir_funcion(sigma, tau, flag):
    x, y = coordenadas_parabolicas(sigma, tau)
    if flag == 1:
        return x - y
    
    elif flag == 2:
        return x**2 + y**2 - 1
    
    elif flag == 3:
        return (((x - (1/2)) + (y - ((1/2))**2))*4) -1
    
    else: #Si la flag es 4 u otra
        return -2-x-y

# Aqui se define la función para graficar
def graficar(values, Title):
    plt.figure(figsize=(10, 6))
    plt.contourf(sigma, tau, values, levels=np.linspace(-1, 1, 100), cmap='plasma')
    plt.colorbar(label='Function Value')
    plt.title('Coordenadas Elipticas: ' + Title)
    plt.xlabel('sigma')
    plt.ylabel('tau')
    plt.contour(sigma, tau, values, levels=[0], colors='cyan')  # Plot function as a red line
    plt.show()

# Aqui se definen los rangos para sigma y tau
sigma_range = np.linspace(-2, 2, 100) #en [-2, 2]
tau_range = np.linspace(-2, 2, 100) #en [-2, 2]

# Aqui se pasan a una malla (Esto ya es de programación en general)
sigma, tau = np.meshgrid(sigma_range, tau_range)

# Aqui asignamos las funciones a graficar
funcion1 = definir_funcion(sigma, tau, 1) # x = y
funcion2 = definir_funcion(sigma, tau, 2) # x^2 + y^2 = 1
funcion3 = definir_funcion(sigma, tau, 3) # (x - 1/2) + (y - 1/2)^2 = 1/4

# Se grafican (y se pone el texto que aparecerá en la gráfica)
graficar(funcion1,'x = y')
graficar(funcion2,'x^2 + y^2 = 1')
graficar(funcion3,'(x - 1/2) + (y - 1/2)^2 = 1/4')

# Hacemo todo de nuevo para la 4 ya que nos cambian los rangos
sigma_range = np.linspace(-3, 1 * np.pi, 100) #en [-3, 1]
tau_range = np.linspace(-3, 1, 100)
sigma, tau = np.meshgrid(sigma_range, tau_range)
funcion4 = definir_funcion(sigma, tau, 4) # -2-x-y
graficar(funcion4,'y = -2-x')
