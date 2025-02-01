"""
Crea una caché con política de reemplazo Least Recently Used (LRU) usando OrderedDict.
"""
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacidad):
        self.cache = OrderedDict()
        self.capacidad = capacidad

    def get(self, clave):
        if clave in self.cache:
            self.cache.move_to_end(clave)
            return self.cache[clave]
        return -1

    def put(self, clave, valor):
        if clave in self.cache:
            self.cache.move_to_end(clave)
        elif len(self.cache) >= self.capacidad:
            self.cache.popitem(last=False)
        self.cache[clave] = valor

lru = LRUCache(3)
lru.put(1, "A")
lru.put(2, "B")
lru.put(3, "C")
lru.get(1)  # Accede al elemento 1
lru.put(4, "D")  # Elimina el menos usado (2)
print(lru.cache)
