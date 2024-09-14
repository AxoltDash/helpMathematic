# Importamos las librerías necesarias
import matplotlib.pyplot as plt
import numpy as np

# Creamos la clase histograma
class Histograma:
    def __init__(self, datos):
        # Inicializa la clase con un conjunto de datos
        self.datos = datos

    # Definimos el método para graficar los histogramas de frecuencia
    def graficar_frecuencia(self, bins=9): # bins es el número de divisiones o barras en el histograma
        plt.hist(self.datos, bins=bins, color='lightsteelblue', edgecolor='black')
        plt.title('Histograma de Frecuencia')
        plt.xlabel('Valor')
        plt.ylabel('Frecuencia')
        plt.grid(True)
        plt.show()

    # Definimos el método para graficar los histogramas de frecuencias relativa
    def graficar_frecuencia_relativa(self, bins=9):
        total_datos = len(self.datos)
        counts, edges = np.histogram(self.datos, bins=bins)
        frecuencias_relativas = counts / total_datos

        # Grafica la frecuencia relativa
        plt.bar(edges[:-1], frecuencias_relativas, width=np.diff(edges), color='thistle', edgecolor='black', align='edge')
        plt.title('Histograma de Frecuencia Relativa')
        plt.xlabel('Valor')
        plt.ylabel('Frecuencia Relativa')
        plt.grid(True)
        plt.show()


datos = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5] # Creamos el conjunto de datos
hist = Histograma(datos)
hist.graficar_frecuencia()
hist.graficar_frecuencia_relativa()

# Transcribimos los datos de cada columna en listas
columna_1 = [0.25, 0.87, 0.53, 0.22, 0.67, 0.14, 0.93, 0.75, 0.45, 0.56]
columna_2 = [0.30, 1.11, 0.50, 0.90, 0.72, 1.23, 0.15, 2.10, 0.67, 1.43]
columna_3 = [1, 3, 2, 1, 4, 2, 3, 1, 5, 2]
columna_4 = [0.01, 0.76, 0.91, 0.03, 0.65, 0.99, 0.12, 0.84, 0.32, 0.58]

# Creamos y graficamos los histogramas para cada columna
for i, datos in enumerate([columna_1, columna_2, columna_3, columna_4], start=1):
    print(f"Histogramas para la Columna {i}:")
    hist = Histograma(datos)
    hist.graficar_frecuencia()
    hist.graficar_frecuencia_relativa()