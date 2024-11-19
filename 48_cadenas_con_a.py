"""
Escribe una función que reciba una lista de cadenas y devuelva 
una nueva lista con las cadenas que contienen la letra 'a'.
"""
def cadenas_con_a(lista_cadenas):
    return [cadena for cadena in lista_cadenas if 'a' in cadena]


lista = ["manzana", "pera", "uva", "plátano"]
print(cadenas_con_a(lista))
