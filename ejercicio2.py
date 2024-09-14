# Importamos las librerías necesarias
import matplotlib.pyplot as plt
import numpy as np
from ejercicio1 import Histograma

# Creamos la clase HistogramaExtendido que hereda de Histograma
class HistogramaExtendido(Histograma):
    # Definimos el método para graficar el histograma de probabilidades acumuladas
    def graficar_probabilidad_acumulada(self, bins=9):
        total_datos = len(self.datos)
        counts, edges = np.histogram(self.datos, bins=bins)
        frecuencias_relativas = counts / total_datos
        probabilidades_acumuladas = np.cumsum(frecuencias_relativas)

        # Grafica la probabilidad acumulada
        plt.step(edges[:-1], probabilidades_acumuladas, where='mid', color='mediumseagreen', linewidth=2)
        plt.title('Histograma de Probabilidad Acumulada')
        plt.xlabel('Valor')
        plt.ylabel('Probabilidad Acumulada')
        plt.grid(True)
        plt.show()

# Ejemplo de uso
if __name__ == "__main__":
    datos = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5] # Creamos el conjunto de datos
    hist_ext = HistogramaExtendido(datos)
    hist_ext.graficar_frecuencia()
    hist_ext.graficar_frecuencia_relativa()
    hist_ext.graficar_probabilidad_acumulada()

    # Transcribimos los datos de cada columna en listas
    columna_1 = [0.25, 0.87, 0.53, 0.22, 0.67, 0.14, 0.93, 0.75, 0.45, 0.56]
    columna_2 = [0.30, 1.11, 0.50, 0.90, 0.72, 1.23, 0.15, 2.10, 0.67, 1.43]
    columna_3 = [1, 3, 2, 1, 4, 2, 3, 1, 5, 2]
    columna_4 = [0.01, 0.76, 0.91, 0.03, 0.65, 0.99, 0.12, 0.84, 0.32, 0.58]

    # Creamos y graficamos los histogramas para cada columna
    for i, datos in enumerate([columna_1, columna_2, columna_3, columna_4], start=1):
        print(f"Histogramas para la Columna {i}:")
        hist_ext = HistogramaExtendido(datos)
        hist_ext.graficar_frecuencia()
        hist_ext.graficar_frecuencia_relativa()
        hist_ext.graficar_probabilidad_acumulada()