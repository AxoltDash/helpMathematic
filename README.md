## Antes de empezar
### Instalación de Bibliotecas:
Puedes instalar las biblio desde tu terminal, si estas usando Visual Studio Code puedes abrir la terminal con Ctrl + `

En este caso usaremos python en un entorno de desarrollo para evitar conflictos con los packetes preefinidos de python (No se porque me maraca error si no es asi XD)

Para ello si usas vs code sigue las siguientes instrucciones:

**Crear un entorno virtual**:
   - Abre VS Code y abre la carpeta de tu proyecto.
   - Abre una nueva terminal integrada en VS Code (`Ctrl + `).
   - Crea un entorno virtual con el siguiente comando:
     ```bash
     python -m venv .venv
     ```
   - Activa el entorno virtual:
     - En Windows:
       ```bash
       .venv\Scripts\activate
       ```
     - En macOS/Linux:
       ```bash
       source .venv/bin/activate
       ```

3. **Seleccionar el intérprete de Python**:
   - En VS Code, abre la paleta de comandos (`Ctrl + Shift + P`) y escribe `Python: Select Interpreter`.
   - Selecciona el entorno virtual que acabas de crear (`.venv`).

##### Ejercicio 1:
```bash
pip install matplotlib
pip install numpy
```

# Explicación del código (GitHub Copilot)
### Ejercicio 1:

Definición de la clase Histograma:
```python
class Histograma:
    def __init__(self, datos):
        self.datos = datos
```
La clase Histograma tiene un método constructor __init__ que inicializa la instancia con un conjunto de datos (datos).

Método para graficar histogramas de frecuencia:
```python
def graficar_frecuencia(self, bins=9):
    plt.hist(self.datos, bins=bins, color='lightsteelblue', edgecolor='black')
    plt.title('Histograma de Frecuencia')
    plt.xlabel('Valor')
    plt.ylabel('Frecuencia')
    plt.grid(True)
    plt.show()
```
Este método utiliza matplotlib para graficar un histograma de frecuencia.
bins define el número de divisiones o barras en el histograma.
Se configuran el título, las etiquetas de los ejes y la cuadrícula antes de mostrar el gráfico.

Método para graficar histogramas de frecuencia relativa:
```python
def graficar_frecuencia_relativa(self, bins=9):
    total_datos = len(self.datos)
    counts, edges = np.histogram(self.datos, bins=bins)
    frecuencias_relativas = counts / total_datos

    plt.bar(edges[:-1], frecuencias_relativas, width=np.diff(edges), color='thistle', edgecolor='black', align='edge')
    plt.title('Histograma de Frecuencia Relativa')
    plt.xlabel('Valor')
    plt.ylabel('Frecuencia Relativa')
    plt.grid(True)
    plt.show()
```
Este método calcula la frecuencia relativa de los datos y luego grafica un histograma de frecuencia relativa.
np.histogram se usa para obtener los conteos y los bordes de los bins.
Se calcula la frecuencia relativa dividiendo los conteos por el total de datos.
Se configura el gráfico de barras con plt.bar y se muestran las etiquetas y la cuadrícula.

Creación y graficación de histogramas:
```python
datos = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
hist = Histograma(datos)
hist.graficar_frecuencia()
hist.graficar_frecuencia_relativa()
```
Se crea un conjunto de datos y se instancia la clase Histograma con estos datos.
Se llaman los métodos para graficar el histograma de frecuencia y el histograma de frecuencia relativa.

Transcripción de datos y graficación para múltiples columnas:
```python
columna_1 = [0.25, 0.87, 0.53, 0.22, 0.67, 0.14, 0.93, 0.75, 0.45, 0.56]
columna_2 = [0.30, 1.11, 0.50, 0.90, 0.72, 1.23, 0.15, 2.10, 0.67, 1.43]
columna_3 = [1, 3, 2, 1, 4, 2, 3, 1, 5, 2]
columna_4 = [0.01, 0.76, 0.91, 0.03, 0.65, 0.99, 0.12, 0.84, 0.32, 0.58]

for i, datos in enumerate([columna_1, columna_2, columna_3, columna_4], start=1):
    print(f"Histogramas para la Columna {i}:")
    hist = Histograma(datos)
    hist.graficar_frecuencia()
    hist.graficar_frecuencia_relativa()
```
Se definen cuatro listas de datos, cada una representando una columna.
Se itera sobre estas listas, creando un histograma para cada una y graficando tanto la frecuencia como la frecuencia relativa.
Este código es útil para visualizar la distribución de datos en diferentes columnas mediante histogramas.
