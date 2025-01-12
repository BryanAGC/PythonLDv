"""
Simula el lanzamiento de dos dados y devuelve el resultado.
"""
import random

def lanzar_dados():
    return random.randint(1, 6), random.randint(1, 6)

# Ejemplo de uso
print(lanzar_dados())
