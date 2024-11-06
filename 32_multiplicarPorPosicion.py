"""
Escribe una función que reciba una lista de números y devuelva una nueva lista 
donde cada número se multiplica por su posición en la lista (es decir, el índice).
"""

def multiplicar_por_indice(lista_numeros):
    return [numero * indice for indice, numero in enumerate(lista_numeros)]

# Ejemplo de uso
lista = [1, 2, 3, 4]
resultado = multiplicar_por_indice(lista)
print(f"Lista con cada número multiplicado por su posición: {resultado}")
