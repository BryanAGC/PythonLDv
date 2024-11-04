"""
Escribe una función que reciba una lista de palabras y devuelva la palabra más larga de la lista. 
Si hay varias palabras con la misma longitud, puedes devolver cualquiera de ellas.

"""
def palabra_mas_larga(lista_palabras):
    palabra_larga = ""
    for palabra in lista_palabras:
        if len(palabra) > len(palabra_larga):  # Verifica si la palabra actual es más larga
            palabra_larga = palabra
    return palabra_larga

# Ejemplo de uso
lista = ["manzana", "pera", "banana", "naranja"]
resultado = palabra_mas_larga(lista)
print(f"La palabra más larga en la lista es: {resultado}")
