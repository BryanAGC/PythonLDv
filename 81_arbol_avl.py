"""
Implementa un árbol AVL que soporte inserciones y mantenga el balance.
"""
class NodoAVL:
    def __init__(self, valor):
        self.valor = valor
        self.altura = 1
        self.izq = None
        self.der = None

class ArbolAVL:
    def obtener_altura(self, nodo):
        return nodo.altura if nodo else 0

    def balance(self, nodo):
        return self.obtener_altura(nodo.izq) - self.obtener_altura(nodo.der) if nodo else 0

    def rotar_derecha(self, nodo):
        nueva_raiz = nodo.izq
        nodo.izq = nueva_raiz.der
        nueva_raiz.der = nodo
        nodo.altura = 1 + max(self.obtener_altura(nodo.izq), self.obtener_altura(nodo.der))
        nueva_raiz.altura = 1 + max(self.obtener_altura(nueva_raiz.izq), self.obtener_altura(nueva_raiz.der))
        return nueva_raiz

    def rotar_izquierda(self, nodo):
        nueva_raiz = nodo.der
        nodo.der = nueva_raiz.izq
        nueva_raiz.izq = nodo
        nodo.altura = 1 + max(self.obtener_altura(nodo.izq), self.obtener_altura(nodo.der))
        nueva_raiz.altura = 1 + max(self.obtener_altura(nueva_raiz.izq), self.obtener_altura(nueva_raiz.der))
        return nueva_raiz

    def insertar(self, nodo, valor):
        if not nodo:
            return NodoAVL(valor)
        if valor < nodo.valor:
            nodo.izq = self.insertar(nodo.izq, valor)
        else:
            nodo.der = self.insertar(nodo.der, valor)
        nodo.altura = 1 + max(self.obtener_altura(nodo.izq), self.obtener_altura(nodo.der))
        balance = self.balance(nodo)
        if balance > 1:
            if valor < nodo.izq.valor:
                return self.rotar_derecha(nodo)
            else:
                nodo.izq = self.rotar_izquierda(nodo.izq)
                return self.rotar_derecha(nodo)
        if balance < -1:
            if valor > nodo.der.valor:
                return self.rotar_izquierda(nodo)
            else:
                nodo.der = self.rotar_derecha(nodo.der)
                return self.rotar_izquierda(nodo)
        return nodo

# Ejemplo de uso
arbol = ArbolAVL()
raiz = None
valores = [10, 20, 30, 40, 50, 25]
for valor in valores:
    raiz = arbol.insertar(raiz, valor)
