"""
Implementa el Algoritmo de Kruskal para encontrar el Árbol de Expansión Mínima en un grafo.
"""
class Grafo:
    def __init__(self, vertices):
        self.V = vertices
        self.aristas = []

    def agregar_arista(self, u, v, peso):
        self.aristas.append((peso, u, v))

    def find(self, padre, i):
        if padre[i] == i:
            return i
        return self.find(padre, padre[i])

    def union(self, padre, rango, x, y):
        raiz_x, raiz_y = self.find(padre, x), self.find(padre, y)
        if rango[raiz_x] < rango[raiz_y]:
            padre[raiz_x] = raiz_y
        elif rango[raiz_x] > rango[raiz_y]:
            padre[raiz_y] = raiz_x
        else:
            padre[raiz_y] = raiz_x
            rango[raiz_x] += 1

    def kruskal(self):
        self.aristas.sort()
        padre, rango = {}, {}
        for v in range(self.V):
            padre[v] = v
            rango[v] = 0
        mst = []
        for peso, u, v in self.aristas:
            if self.find(padre, u) != self.find(padre, v):
                self.union(padre, rango, u, v)
                mst.append((u, v, peso))
        return mst

g = Grafo(4)
g.agregar_arista(0, 1, 10)
g.agregar_arista(0, 2, 6)
g.agregar_arista(0, 3, 5)
g.agregar_arista(1, 3, 15)
g.agregar_arista(2, 3, 4)
print(g.kruskal())
