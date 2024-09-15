# Importamos las librerías necesarias
import matplotlib.pyplot as plt
import numpy as np
from ejercicio1 import Histograma
from ejercicio2 import HistogramaExtendido

class MapeoLogistico:
    def __init__(self, r, x0, n):
        self.r = r
        self.x0 = x0
        self.n = n
        self.datos = self.simular()

    def simular(self):
        x = self.x0
        datos = [x]
        for _ in range(self.n - 1):
            x = self.r * x * (1 - x)
            datos.append(x)
        return datos

if __name__ == "__main__":
    # Parámetros del mapeo logístico
    r = 4
    x0 = 0.5
    n = 1000

    # Crear instancia de MapeoLogistico y generar datos
    mapeo = MapeoLogistico(r, x0, n)
    datos = mapeo.datos

    # Crear instancia de HistogramaExtendido y graficar
    hist_ext = HistogramaExtendido(datos)
    hist_ext.graficar_frecuencia()
    hist_ext.graficar_frecuencia_relativa()
    hist_ext.graficar_probabilidad_acumulada()

    print("Histograma Extendido:")
    hist_ext = HistogramaExtendido(datos)