"""
Escribe una función que reciba un grafo representado como un diccionario y dos nodos. 
Determina si existe un camino entre los dos nodos utilizando una búsqueda en profundidad (DFS).
"""
def existe_camino(grafo, inicio, fin, visitados=None):
    if visitados is None:
        visitados = set()
    if inicio == fin:
        return True
    visitados.add(inicio)
    for vecino in grafo.get(inicio, []):
        if vecino not in visitados:
            if existe_camino(grafo, vecino, fin, visitados):
                return True
    return False

# Ejemplo de uso
grafo = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': ['F'],
    'E': ['F'],
    'F': []
}
print(existe_camino(grafo, 'A', 'F'))  # True
print(existe_camino(grafo, 'A', 'G'))  # False
