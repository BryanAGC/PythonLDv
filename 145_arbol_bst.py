"""
Implementa un Árbol Binario de Búsqueda con inserción y recorrido inorden.
"""
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

class BST:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if not self.raiz:
            self.raiz = Nodo(valor)
        else:
            self._insertar(self.raiz, valor)

    def _insertar(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izq:
                self._insertar(nodo.izq, valor)
            else:
                nodo.izq = Nodo(valor)
        else:
            if nodo.der:
                self._insertar(nodo.der, valor)
            else:
                nodo.der = Nodo(valor)

    def inorden(self, nodo):
        if nodo:
            self.inorden(nodo.izq)
            print(nodo.valor, end=" ")
            self.inorden(nodo.der)

# Ejemplo de uso
bst = BST()
valores = [10, 5, 15, 2, 7, 12, 18]
for v in valores:
    bst.insertar(v)

bst.inorden(bst.raiz)  # 2 5 7 10 12 15 18
