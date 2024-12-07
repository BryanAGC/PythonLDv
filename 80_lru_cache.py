"""
Implementa una clase para gestionar una caché de tipo LRU (Least Recently Used).
"""
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacidad):
        self.cache = OrderedDict()
        self.capacidad = capacidad

    def get(self, clave):
        if clave not in self.cache:
            return -1
        self.cache.move_to_end(clave)
        return self.cache[clave]

    def put(self, clave, valor):
        if clave in self.cache:
            self.cache.move_to_end(clave)
        self.cache[clave] = valor
        if len(self.cache) > self.capacidad:
            self.cache.popitem(last=False)

# Ejemplo de uso
cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))  # 1
cache.put(3, 3)
print(cache.get(2))  # -1
