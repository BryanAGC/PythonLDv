"""
Escribe una función que reciba una lista de palabras y devuelva un diccionario con la longitud de cada palabra.
"""
def longitud_palabras(lista_palabras):
    return {palabra: len(palabra) for palabra in lista_palabras}


print(longitud_palabras(["hola", "mundo", "python"]))  # {'hola': 4, 'mundo': 5, 'python': 6}
