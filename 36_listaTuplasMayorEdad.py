"""
Escribe una función que reciba una lista de tuplas, donde cada tupla contiene un nombre y una edad.
La función debe devolver el nombre de la persona más joven.
"""

def persona_mas_joven(lista_personas):

    persona_joven = min(lista_personas, key=lambda x: x[1])
    return persona_joven[0]  

lista = [("Juan", 25), ("Ana", 22), ("Pedro", 30)]
resultado = persona_mas_joven(lista)
print(f"La persona más joven es: {resultado}")
