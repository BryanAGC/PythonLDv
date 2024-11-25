"""
Implementa el algoritmo de Dijkstra para encontrar la distancia más corta desde un nodo de inicio 
a todos los demás nodos en un grafo ponderado representado como un diccionario.
"""
import heapq

def dijkstra(grafo, inicio):
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[inicio] = 0
    prioridad = [(0, inicio)]
    
    while prioridad:
        distancia_actual, nodo_actual = heapq.heappop(prioridad)
        
        if distancia_actual > distancias[nodo_actual]:
            continue
        
        for vecino, peso in grafo[nodo_actual].items():
            distancia = distancia_actual + peso
            if distancia < distancias[vecino]:
                distancias[vecino] = distancia
                heapq.heappush(prioridad, (distancia, vecino))
    
    return distancias

# Ejemplo de uso
grafo = {
    'A': {'B': 1, 'C': 4},
    'B': {'C': 2, 'D': 5},
    'C': {'D': 1},
    'D': {}
}
print(dijkstra(grafo, 'A'))  # {'A': 0, 'B': 1, 'C': 3, 'D': 4}
