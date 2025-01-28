"""
Encuentra cuántas componentes conexas tiene un grafo no dirigido.
"""
def dfs(nodo, visitados, grafo):
    visitados.add(nodo)
    for vecino in grafo[nodo]:
        if vecino not in visitados:
            dfs(vecino, visitados, grafo)

def contar_componentes(grafo):
    visitados = set()
    componentes = 0
    for nodo in grafo:
        if nodo not in visitados:
            dfs(nodo, visitados, grafo)
            componentes += 1
    return componentes

grafo = {
    0: [1],
    1: [0, 2],
    2: [1],
    3: [4],
    4: [3]
}

print(contar_componentes(grafo))
