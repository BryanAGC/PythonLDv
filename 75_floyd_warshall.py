"""
Implementa el algoritmo de Floyd-Warshall para encontrar los caminos más cortos entre todos los pares de nodos en un grafo ponderado.
"""
def floyd_warshall(grafo):
    dist = [[float('inf')] * len(grafo) for _ in range(len(grafo))]
    for i in range(len(grafo)):
        dist[i][i] = 0
        for j, peso in grafo[i]:
            dist[i][j] = peso

    for k in range(len(grafo)):
        for i in range(len(grafo)):
            for j in range(len(grafo)):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist


grafo = [
    [(1, 3), (2, 1)],
    [(2, 7), (3, 5)],
    [(3, 2)],
    []
]
print(floyd_warshall(grafo))
