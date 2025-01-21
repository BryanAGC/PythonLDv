"""
Encuentra los componentes fuertemente conectados en un grafo dirigido usando Kosaraju.
"""
from collections import defaultdict

class Grafo:
    def __init__(self, vertices):
        self.V = vertices
        self.grafo = defaultdict(list)
    
    def agregar_arista(self, u, v):
        self.grafo[u].append(v)

    def dfs(self, v, visitado, pila):
        visitado[v] = True
        for vecino in self.grafo[v]:
            if not visitado[vecino]:
                self.dfs(vecino, visitado, pila)
        pila.append(v)

    def transponer(self):
        grafo_t = Grafo(self.V)
        for v in self.grafo:
            for vecino in self.grafo[v]:
                grafo_t.agregar_arista(vecino, v)
        return grafo_t

    def encontrar_scc(self):
        pila, visitado = [], [False] * self.V
        for v in range(self.V):
            if not visitado[v]:
                self.dfs(v, visitado, pila)

        grafo_t = self.transponer()
        visitado = [False] * self.V

        while pila:
            v = pila.pop()
            if not visitado[v]:
                componente = []
                grafo_t.dfs(v, visitado, componente)
                print("Componente fuertemente conectada:", componente)

# Ejemplo de uso
g = Grafo(5)
g.agregar_arista(0, 2)
g.agregar_arista(2, 1)
g.agregar_arista(1, 0)
g.agregar_arista(0, 3)
g.agregar_arista(3, 4)
g.encontrar_scc()
