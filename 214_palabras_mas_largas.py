"""
Escribe una función que reciba una lista de palabras y devuelva las palabras más largas.
"""
def palabras_mas_largas(lista_palabras):
    max_longitud = max(len(palabra) for palabra in lista_palabras)
    return [palabra for palabra in lista_palabras if len(palabra) == max_longitud]

# Ejemplo de uso
palabras = ["python", "java", "javascript", "c++"]
resultado = palabras_mas_largas(palabras)
print(f"Las palabras más largas son: {resultado}")
