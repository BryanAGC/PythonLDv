"""
Implementa un Trie para almacenar palabras y realizar búsquedas eficientes por prefijo.
"""
class TrieNode:
    def __init__(self):
        self.hijos = {}
        self.fin_palabra = False

class Trie:
    def __init__(self):
        self.raiz = TrieNode()

    def insertar(self, palabra):
        nodo = self.raiz
        for letra in palabra:
            if letra not in nodo.hijos:
                nodo.hijos[letra] = TrieNode()
            nodo = nodo.hijos[letra]
        nodo.fin_palabra = True

    def buscar(self, palabra):
        nodo = self.raiz
        for letra in palabra:
            if letra not in nodo.hijos:
                return False
            nodo = nodo.hijos[letra]
        return nodo.fin_palabra

trie = Trie()
trie.insertar("casa")
trie.insertar("carro")
print(trie.buscar("casa"))  # True
print(trie.buscar("cama"))  # False
