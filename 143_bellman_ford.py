"""
Implementa el algoritmo de Bellman-Ford para encontrar los caminos más cortos en un grafo con pesos negativos.
"""
def bellman_ford(grafo, inicio, n):
    dist = {nodo: float('inf') for nodo in grafo}
    dist[inicio] = 0

    for _ in range(n - 1):
        for u in grafo:
            for v, peso in grafo[u]:
                if dist[u] + peso < dist[v]:
                    dist[v] = dist[u] + peso

    return dist

# Grafo con pesos negativos
grafo = {
    0: [(1, 4), (2, 5)],
    1: [(2, -3)],
    2: [(3, 2)],
    3: []
}

print(bellman_ford(grafo, 0, 4))
