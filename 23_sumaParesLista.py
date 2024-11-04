"""
ESCRIBE UNA FUNCIÓN QUE TOME UNA LISTA DE NÚMEROS ENTEROS Y DEVUELVA LA SUMA DE TODOS LOS NÚMEROS PARES EN LA LISTA.
"""
def suma_pares(lista_numeros):
    suma = 0
    for numero in lista_numeros:
        if numero % 2 == 0:  
            suma += numero
    return suma


lista = [1, 2, 3, 4, 5, 6]
resultado = suma_pares(lista)
print(f"La suma de los números pares en la lista es: {resultado}")
