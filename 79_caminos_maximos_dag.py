"""
Dado un grafo dirigido acíclico (DAG) y un nodo origen, encuentra el camino máximo hacia cualquier otro nodo.
"""
from collections import defaultdict, deque

from collections import defaultdict, deque

def caminos_maximos_dag(grafo, origen):
    def ordenar_topologico(grafo):
        grados_entrada = defaultdict(int)
        for nodo in grafo:
            for vecino, _ in grafo[nodo]:  # Solo el nodo vecino, ignorar el peso
                grados_entrada[vecino] += 1
        cola = deque([nodo for nodo in grafo if grados_entrada[nodo] == 0])
        orden = []
        while cola:
            actual = cola.popleft()
            orden.append(actual)
            for vecino, _ in grafo[actual]:  # Solo el nodo vecino
                grados_entrada[vecino] -= 1
                if grados_entrada[vecino] == 0:
                    cola.append(vecino)
        return orden

    orden = ordenar_topologico(grafo)
    distancias = {nodo: float('-inf') for nodo in grafo}
    distancias[origen] = 0

    for nodo in orden:
        for vecino, peso in grafo[nodo]:
            if distancias[nodo] + peso > distancias[vecino]:
                distancias[vecino] = distancias[nodo] + peso

    return distancias

# Ejemplo de uso
grafo = {
    'A': [('B', 3), ('C', 2)],
    'B': [('D', 4)],
    'C': [('D', 1)],
    'D': []
}
print(caminos_maximos_dag(grafo, 'A'))  # {'A': 0, 'B': 3, 'C': 2, 'D': 7}
