import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# Definir los nombres de los nodos
nombres_nodos = ['A', 'B', 'C', 'D', 'E']

# Definir la matriz inicial
matriz_inicial = np.array([
    [0, 0, 0.333333333, 0.5, 0],
    [0.5, 0, 0, 0.5, 0],
    [0, 0.5, 0, 0, 0],
    [0.5, 0.5, 0.333333333, 0, 1],
    [0, 0, 0.333333333, 0, 0]
])

# Crear un grafo dirigido
G = nx.DiGraph()

# Agregar nodos al grafo
for i, nombre in enumerate(nombres_nodos):
    G.add_node(nombre)

# Agregar arcos al grafo según la matriz inicial
for i in range(matriz_inicial.shape[0]):
    for j in range(matriz_inicial.shape[1]):
        if matriz_inicial[i, j] != 0:
            G.add_edge(nombres_nodos[i], nombres_nodos[j], weight=matriz_inicial[i, j])

# Dibujar el grafo con etiquetas de nodos y flechas
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, arrows=True)
plt.show()


# Definir la matriz de transiciones
matriz_transiciones = np.array([0.2, 0.2, 0.2, 0.2, 0.2])

# Función objetivo para el método de Newton-Raphson
def diferencia_matriz(matriz_nueva, matriz_anterior):
    return np.max(np.abs(matriz_nueva - matriz_anterior))

# Tolerancia para detener las iteraciones
tolerancia = 0.000001
# Calcular el resultado para la primera iteración
matriz_resultante = np.sum(matriz_inicial * matriz_transiciones, axis=1)

# Imprimir la matriz resultante inicial
print("Matriz resultante inicial:")
print(matriz_resultante)
suma = np.sum(matriz_resultante)
print("total= ", suma)

# Inicializar la variable de diferencia
diferencia = np.inf  # Inicializar la diferencia como infinito para comenzar el bucle

# Iterar usando un bucle while hasta que la diferencia sea menor o igual a la tolerancia
iteracion = 0
while diferencia > tolerancia:
    matriz_nueva = np.sum(matriz_inicial * matriz_resultante[:, None], axis=1)

    # Imprimir la matriz nueva en cada iteración
    suma_total = np.sum(matriz_nueva)
    matriz_nueva_normalizada = matriz_nueva / suma_total

    # Imprimir la matriz nueva normalizada
    print(f'\nIteración {iteracion+1}:')
    print(matriz_nueva_normalizada)
    print("total= ", np.sum(matriz_nueva_normalizada))

    # Calcular la diferencia entre la matriz anterior y la nueva
    for i in range(len(matriz_nueva)):
        diferencia = np.abs(matriz_nueva_normalizada[i] - matriz_resultante[i])
        if diferencia <= tolerancia:
            print(diferencia)
            break

    # Actualizar la matriz resultante para la siguiente iteración
    matriz_resultante = matriz_nueva_normalizada
    iteracion += 1

print(f'\nSe detuvo la iteración en la {iteracion}-ésima iteración porque la diferencia es menor o igual a la tolerancia ({tolerancia}).')
