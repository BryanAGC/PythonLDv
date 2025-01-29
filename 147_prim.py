"""
Implementa el algoritmo de Prim para encontrar el Árbol de Expansión Mínima (MST) en un grafo ponderado.
"""
import heapq

def prim(grafo, inicio):
    mst = []
    visitados = set()
    heap = [(0, inicio, None)]

    while heap:
        costo, nodo, padre = heapq.heappop(heap)
        if nodo not in visitados:
            visitados.add(nodo)
            if padre is not None:
                mst.append((padre, nodo, costo))
            for vecino, peso in grafo[nodo]:
                if vecino not in visitados:
                    heapq.heappush(heap, (peso, vecino, nodo))
    
    return mst

grafo = {
    0: [(1, 2), (3, 6)],
    1: [(0, 2), (2, 3), (3, 8), (4, 5)],
    2: [(1, 3), (4, 7)],
    3: [(0, 6), (1, 8)],
    4: [(1, 5), (2, 7)]
}

print(prim(grafo, 0))
