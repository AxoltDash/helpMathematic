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

def graficar_elipticas():
    # Graficar cuadrícula cartesiana transformada
    mu_vals = np.linspace(0.1, 2, 20)  # Evitamos mu = 0 para evitar singularidad en cosh
    nu_vals = np.linspace(0, 2*np.pi, 200)

    plt.figure(figsize=(6,6))

    # Graficar líneas de la cuadrícula elíptica
    for mu in mu_vals:
        X, Y = elipticas(mu, nu_vals)
        plt.plot(X, Y, 'b', lw=1)  # Líneas azules para la cuadrícula

    for nu in np.linspace(0, 2*np.pi, 30):
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



# Función de transformación parabólica
def parabolicas(xi, eta):
    x = xi * eta
    y = 0.5 * (xi**2 - eta**2)
    return x, y

def graficar_paraboloicas():
    # Graficar cuadrícula cartesiana transformada
    xi_vals = np.linspace(-2, 2, 20)
    eta_vals = np.linspace(-2, 2, 5)

    plt.figure(figsize=(6,6))

    # Graficar líneas de la cuadrícula parabólica
    for xi in xi_vals:
        eta_vals = np.linspace(-2, 2, 50)
        X, Y = parabolicas(xi, eta_vals)
        plt.plot(X, Y, 'r', lw=1)  # Líneas azules para la cuadrícula

    for eta in eta_vals:
        xi_vals = np.linspace(-2, 2, 20)
        X, Y = parabolicas(xi_vals, eta)
        plt.plot(X, Y, 'b', lw=1)  # Líneas rojas para la cuadrícula

    plt.title("Cuadrícula cartesiana transformada a coordenadas parabólicas")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.axis('equal')
    plt.show()

    # Cálculo del factor de cambio de área (Jacobiano)
    xi, eta = sp.symbols('xi eta')
    x = 0.5 * (xi**2 - eta**2)
    y = xi * eta

    # Derivadas parciales para el Jacobiano
    J = sp.Matrix([[sp.diff(x, xi), sp.diff(x, eta)],
                [sp.diff(y, xi), sp.diff(y, eta)]])

    # Determinante del Jacobiano
    det_J = J.det()
    det_J_simplified = sp.simplify(det_J)
    print("Factor de cambio de área (determinante del Jacobiano) para coordenadas parabólicas:")
    sp.pprint(det_J_simplified)



# Función de transformación bipolar
def bipolares(mu, nu, a=1):
    x = a * np.sinh(mu) / (np.cosh(mu) - np.cos(nu))
    y = a * np.sin(nu) / (np.cosh(mu) - np.cos(nu))
    return x, y

def graficar_bipolares():
    # Graficar cuadrícula cartesiana transformada
    mu_vals = np.linspace(-2, 2, 20)
    nu_vals = np.linspace(0, 2*np.pi, 10)

    plt.figure(figsize=(6,6))

    # Graficar líneas de la cuadrícula bipolar
    for mu in mu_vals:
        nu_vals = np.linspace(0, 2*np.pi, 100)
        X, Y = bipolares(mu, nu_vals)
        plt.plot(X, Y, 'b', lw=1)  # Líneas azules para la cuadrícula

    for nu in nu_vals:
        mu_vals = np.linspace(-2, 2, 100)
        X, Y = bipolares(mu_vals, nu)
        plt.plot(X, Y, 'r', lw=1)  # Líneas rojas para la cuadrícula

    plt.title("Cuadrícula cartesiana transformada a coordenadas bipolares")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.xlim(-4,4)
    plt.ylim(-4,4)
    plt.show()

    # Cálculo del factor de cambio de área (Jacobiano)
    mu, nu = sp.symbols('mu nu')
    x = a * sp.sinh(mu) / (sp.cosh(mu) - sp.cos(nu))
    y = a * sp.sin(nu) / (sp.cosh(mu) - sp.cos(nu))

    # Derivadas parciales para el Jacobiano
    J = sp.Matrix([[sp.diff(x, mu), sp.diff(x, nu)],
                [sp.diff(y, mu), sp.diff(y, nu)]])

    # Determinante del Jacobiano
    det_J = J.det()
    det_J_simplified = sp.simplify(det_J)
    print("Factor de cambio de área (determinante del Jacobiano) para coordenadas bipolares:")
    sp.pprint(det_J_simplified)
    
graficar_elipticas()
graficar_paraboloicas()
graficar_bipolares()
