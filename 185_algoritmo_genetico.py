"""
Implementa un algoritmo genético para maximizar una función.
"""
import random

def fitness(x):
    return x**2

def mutar(x):
    return x + random.uniform(-1, 1)

def seleccionar(poblacion):
    return sorted(poblacion, key=fitness, reverse=True)[:len(poblacion)//2]

def algoritmo_genetico():
    poblacion = [random.uniform(-10, 10) for _ in range(10)]
    
    for _ in range(50):
        poblacion = seleccionar(poblacion)
        hijos = [mutar(p) for p in poblacion]
        poblacion.extend(hijos)

    mejor = max(poblacion, key=fitness)
    return mejor

print("Mejor solución encontrada:", algoritmo_genetico())
