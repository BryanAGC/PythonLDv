"""
Implementa un sistema de autocompletado usando una estructura Trie.
"""
class TrieNode:
    def __init__(self):
        self.hijos = {}
        self.es_fin = False

class Trie:
    def __init__(self):
        self.raiz = TrieNode()

    def insertar(self, palabra):
        nodo = self.raiz
        for char in palabra:
            if char not in nodo.hijos:
                nodo.hijos[char] = TrieNode()
            nodo = nodo.hijos[char]
        nodo.es_fin = True

    def buscar(self, prefijo):
        nodo = self.raiz
        for char in prefijo:
            if char not in nodo.hijos:
                return []
            nodo = nodo.hijos[char]
        return self._obtener_palabras(nodo, prefijo)

    def _obtener_palabras(self, nodo, prefijo):
        palabras = []
        if nodo.es_fin:
            palabras.append(prefijo)
        for char, hijo in nodo.hijos.items():
            palabras.extend(self._obtener_palabras(hijo, prefijo + char))
        return palabras

# Ejemplo de uso
trie = Trie()
trie.insertar("gato")
trie.insertar("gallina")
trie.insertar("galaxia")
print(trie.buscar("ga"))  # ["gato", "gallina", "galaxia"]
