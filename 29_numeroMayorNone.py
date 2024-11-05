"""
Escribe una función que reciba una lista de números y devuelva el segundo número más
grande de la lista. Si la lista tiene menos de dos elementos, la función debería devolver None.
"""
def segundo_mas_grande(lista_numeros):
    if len(lista_numeros) < 2:
        return None
    
    lista_unica = list(set(lista_numeros))
    lista_unica.sort(reverse=True)
    
    return lista_unica[1] if len(lista_unica) > 1 else None

lista = [4, 1, 7, 3, 9]
resultado = segundo_mas_grande(lista)
print(f"El segundo número más grande en la lista es: {resultado}")
