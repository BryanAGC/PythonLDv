"""
Escribe una función que detecte si un grafo dirigido tiene un ciclo utilizando el algoritmo de detección de ciclos.
"""
def tiene_ciclo(grafo):
    def dfs(nodo, visitados, pila_recursiva):
        visitados.add(nodo)
        pila_recursiva.add(nodo)
        for vecino in grafo.get(nodo, []):
            if vecino not in visitados:
                if dfs(vecino, visitados, pila_recursiva):
                    return True
            elif vecino in pila_recursiva:
                return True
        pila_recursiva.remove(nodo)
        return False

    visitados = set()
    for nodo in grafo:
        if nodo not in visitados:
            if dfs(nodo, visitados, set()):
                return True
    return False


grafo = {
    'A': ['B'],
    'B': ['C'],
    'C': ['A']
}
print(tiene_ciclo(grafo))  # True
