"""
Escribe una función que reciba una lista de números y devuelva el 
número más grande y el más pequeño de la lista en forma de tupla.
"""

def min_max(lista_numeros):
    if not lista_numeros:  
        return None, None
    
    numero_menor = lista_numeros[0]
    numero_mayor = lista_numeros[0]
    
    for numero in lista_numeros:
        if numero < numero_menor:
            numero_menor = numero
        if numero > numero_mayor:
            numero_mayor = numero
            
    return numero_menor, numero_mayor


lista = [3, 7, 1, 9, 4]
resultado = min_max(lista)
print(f"El número más pequeño y más grande es: {resultado}")
