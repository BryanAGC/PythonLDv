"""
Implementa un sistema de autocompletado usando la estructura Trie.
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
        for char in palabra:
            if char not in nodo.hijos:
                nodo.hijos[char] = TrieNode()
            nodo = nodo.hijos[char]
        nodo.fin_palabra = True

    def buscar_palabras(self, prefijo):
        def dfs(nodo, prefijo_actual):
            if nodo.fin_palabra:
                palabras.append(prefijo_actual)
            for char, hijo in nodo.hijos.items():
                dfs(hijo, prefijo_actual + char)

        nodo = self.raiz
        for char in prefijo:
            if char not in nodo.hijos:
                return []
            nodo = nodo.hijos[char]

        palabras = []
        dfs(nodo, prefijo)
        return palabras

trie = Trie()
palabras = ["gato", "gallina", "galaxia", "garra", "gol"]
for palabra in palabras:
    trie.insertar(palabra)

print(trie.buscar_palabras("ga"))  # ['gato', 'gallina', 'galaxia', 'garra']
