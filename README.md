# Proyecto Inferencia Red Bayesiana
## Desarrollado por 🤝️
* Juan Sebastian Angarita

* Santiago Caro

* Jose Carlos Molano

## Archivos Importantes 📂️
* [proyecto.py](proyecto.py)

    Archivo que contiene la lógica que resuelve la inferencia Bayesiana, tiene como entradas los valores de todos los nodos y la pregunta a resolver. Tiene como salidas la probabilidad de la pregunta con números normalizados
* [readFile.py](readFile.py)

    Archivo que contiene la lógica para leer el archivo que contiene la red Bayesiana. Tiene como entrada el nombre del archivo y como salida tiene la red bayesiana en una variable.
* [red.txt](red.txt)
    
    Archivo que contiene la información de la red bayesiana con el siguiente formato:
    * **Columna 1..n-2**: Dependencias de nodos anteriores
    * **Columna n-1**: Valores de estados propios del nodo
    * **Columna n**: Valores de las probabilidades de los acontecimientos descritos en las columnas 1 .. n-1
## Ejecución ▶️

Para la ejecución de este proyecto es necesario tener python3 instalado e instalar numpy.

Para instalar numpy:

``` pip install numpy```

Para ejecutar el proyecto

``` python3 proyecto.py```