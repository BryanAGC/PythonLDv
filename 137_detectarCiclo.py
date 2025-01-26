"""
Usa DFS para detectar ciclos en un grafo dirigido.
"""
def tiene_ciclo(grafo):
    visitados = set()
    pila_recursion = set()

    def dfs(nodo):
        if nodo in pila_recursion:
            return True
        if nodo in visitados:
            return False

        visitados.add(nodo)
        pila_recursion.add(nodo)

        for vecino in grafo.get(nodo, []):
            if dfs(vecino):
                return True

        pila_recursion.remove(nodo)
        return False

    return any(dfs(nodo) for nodo in grafo)

# Ejemplo de uso
grafo = {
    'A': ['B'],
    'B': ['C'],
    'C': ['A']
}

print(tiene_ciclo(grafo))  # True
