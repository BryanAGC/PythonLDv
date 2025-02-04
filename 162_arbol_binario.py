"""
Implementa un árbol binario de búsqueda con inserción y recorrido inorden.
"""
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if not self.raiz:
            self.raiz = Nodo(valor)
        else:
            self._insertar(valor, self.raiz)

    def _insertar(self, valor, nodo_actual):
        if valor < nodo_actual.valor:
            if nodo_actual.izquierda:
                self._insertar(valor, nodo_actual.izquierda)
            else:
                nodo_actual.izquierda = Nodo(valor)
        else:
            if nodo_actual.derecha:
                self._insertar(valor, nodo_actual.derecha)
            else:
                nodo_actual.derecha = Nodo(valor)

    def inorden(self, nodo=None):
        if nodo:
            self.inorden(nodo.izquierda)
            print(nodo.valor, end=" ")
            self.inorden(nodo.derecha)

arbol = ArbolBinario()
for num in [10, 5, 15, 2, 7, 12, 18]:
    arbol.insertar(num)

arbol.inorden(arbol.raiz)  # 2 5 7 10 12 15 18
