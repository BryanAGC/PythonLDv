"""
Implementa el algoritmo de Bellman-Ford para encontrar los caminos más cortos desde un nodo origen.
"""
def bellman_ford(grafo, origen):
    dist = {nodo: float('inf') for nodo in grafo}
    dist[origen] = 0

    for _ in range(len(grafo) - 1):
        for nodo in grafo:
            for vecino, peso in grafo[nodo]:
                if dist[nodo] + peso < dist[vecino]:
                    dist[vecino] = dist[nodo] + peso

    for nodo in grafo:
        for vecino, peso in grafo[nodo]:
            if dist[nodo] + peso < dist[vecino]:
                raise ValueError("El grafo contiene un ciclo negativo.")
    return dist

# Ejemplo de uso
grafo = {
    'A': [('B', 4), ('C', 2)],
    'B': [('C', 1), ('D', 5)],
    'C': [('D', 8)],
    'D': []
}
print(bellman_ford(grafo, 'A'))
