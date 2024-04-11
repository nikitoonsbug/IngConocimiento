import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# Definir los nombres de los nodos
nombres_nodos = ['A', 'B', 'C', 'D', 'E']

# Definir la matriz inicial
matriz_inicial = np.array([
    [0, 0, 0.333333333, 0.5, 0],
    [1, 0, 0, 0.5, 0],
    [0, 0.5, 0, 0, 1],
    [0, 0.5, 0.333333333, 0, 0],
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

# Imprimir la matriz inicial
print("Matriz Inicial:")
print(matriz_inicial)

# Calcular la matriz resultante inicial
matriz_transiciones = np.array([0.2, 0.2, 0.2, 0.2, 0.2])
matriz_resultante_inicial = np.sum(matriz_inicial * matriz_transiciones, axis=1)
print("\nMatriz resultante inicial:")
print(matriz_resultante_inicial)

# Dibujar el grafo inicial con etiquetas de nodos y flechas
plt.figure(figsize=(10, 5))
plt.subplot(1, 3, 1)
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, arrows=True)
plt.title('Grafo Inicial')

matriz_inicial = np.array([
    [0, 0, 0.333333333, 0.5, 0],
    [0, 0, 0, 0.5, 0],
    [0, 0.5, 0, 0, 1],
    [0, 0, 0.333333333, 0, 0],
    [1, 0.5, 0.333333333, 0, 0]
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

# Imprimir la matriz inicial
print("Matriz modificada:")
print(matriz_inicial)

# Calcular la matriz resultante inicial
matriz_transiciones = np.array([0.2, 0.2, 0.2, 0.2, 0.2])
matriz_resultante_inicial = np.sum(matriz_inicial * matriz_transiciones, axis=1)
print("\nMatriz resultante modificada:")
print(matriz_resultante_inicial)

# Dibujar el grafo inicial con etiquetas de nodos y flechas
plt.figure(figsize=(10, 5))
plt.subplot(1, 3, 1)
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, arrows=True)
plt.title('Grafo modificado')