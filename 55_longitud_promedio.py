"""
Escribe una función que reciba una lista de cadenas y devuelva la longitud promedio de las cadenas.
"""
def longitud_promedio(lista_cadenas):
    return sum(len(cadena) for cadena in lista_cadenas) / len(lista_cadenas) if lista_cadenas else 0


print(longitud_promedio(["hola", "mundo", "python"]))  # 5.0
