"""
Convierte una lista con listas anidadas en una lista plana (sin anidación).
"""
def lista_plana(lista):
    resultado = []
    for elemento in lista:
        if isinstance(elemento, list):
            resultado.extend(lista_plana(elemento))
        else:
            resultado.append(elemento)
    return resultado

# Ejemplo de uso
print(lista_plana([1, [2, [3, 4], 5], 6]))  # [1, 2, 3, 4, 5, 6]
