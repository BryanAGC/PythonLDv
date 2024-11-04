"""
Escribe una función que tome una lista de números y devuelva la misma lista, 
pero con cada número elevado al cuadrado."""

def elevar_al_cuadrado(lista_numeros):
    return [numero ** 2 for numero in lista_numeros]

lista = [1, 2, 3, 4, 5]
resultado = elevar_al_cuadrado(lista)
print(f"Lista de números elevados al cuadrado: {resultado}")
