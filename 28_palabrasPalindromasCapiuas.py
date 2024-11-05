"""
Escribe una funcion que devuelva una lista con las palabras
que sean palindromas
"""
def encontrar_palindromos(lista_palabras):
    palindromos = []
    for palabra in lista_palabras:
        if palabra == palabra[::-1]: 
            palindromos.append(palabra)
    return palindromos


lista = ["radar", "sol", "reconocer", "luz", "oso"]
resultado = encontrar_palindromos(lista)
print(f"Palabras palíndromas en la lista: {resultado}")
