"""
Dada una lista de números enteros consecutivos en la que falta un número, 
encuentra y devuelve el número faltante.
"""
def encontrar_faltante(lista):
    return sum(range(lista[0], lista[-1] + 1)) - sum(lista)

# Ejemplo de uso
numeros = [1, 2, 3, 4, 6, 7, 8]
print(encontrar_faltante(numeros))  # 5
