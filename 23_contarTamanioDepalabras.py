"""
Escribe una función que reciba una lista de palabras 
y devuelva una nueva lista con solo las palabras que tienen más de cinco letras
"""

def palabras_largas(lista_palabras):
    return [palabra for palabra in lista_palabras if len(palabra) > 5]


lista = ["perro", "elefante", "gato", "hipopótamo", "sol"]
resultado = palabras_largas(lista)
print(f"Palabras con más de cinco letras: {resultado}")
