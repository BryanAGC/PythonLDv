"""
Escribe una función que reciba un diccionario y lo invierta, cambiando las claves por valores y viceversa.
"""
def invertir_diccionario(diccionario):
    return {v: k for k, v in diccionario.items()}

# Ejemplo de uso
diccionario = {"a": 1, "b": 2, "c": 3}
resultado = invertir_diccionario(diccionario)
print(f"Diccionario invertido: {resultado}")
