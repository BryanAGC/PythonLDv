"""
Resuelve el Problema del Viajero con fuerza bruta y poda.
"""
from itertools import permutations

def distancia_total(ruta, distancias):
    return sum(distancias[ruta[i]][ruta[i+1]] for i in range(len(ruta)-1)) + distancias[ruta[-1]][ruta[0]]

def tsp(distancias):
    ciudades = list(range(len(distancias)))
    rutas = permutations(ciudades)
    return min(distancia_total(ruta, distancias) for ruta in rutas)

distancias = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
print(tsp(distancias))  # Mínima distancia
