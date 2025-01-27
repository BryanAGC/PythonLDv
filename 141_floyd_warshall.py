"""
Implementa el algoritmo de Floyd-Warshall para encontrar los caminos más cortos entre todos los pares de nodos en un grafo ponderado.
"""
def floyd_warshall(grafo):
    n = len(grafo)
    dist = [[float('inf')] * n for _ in range(n)]
    
    for i in range(n):
        dist[i][i] = 0
    
    for u in range(n):
        for v, peso in grafo[u]:
            dist[u][v] = peso
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist

# Representación del grafo como lista de adyacencia
grafo = {
    0: [(1, 3), (2, 5)],
    1: [(2, 1)],
    2: [(3, 2)],
    3: []
}

print(floyd_warshall(grafo))
