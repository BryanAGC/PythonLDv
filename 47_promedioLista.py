"""
Escribe una función que reciba una lista de números y devuelva 
el promedio de los números positivos en la lista. 
Si no hay números positivos, la función debería devolver None.
"""
def promedio_positivos(lista_numeros):
    positivos = [num for num in lista_numeros if num > 0]  # Filtra los números positivos
    if not positivos:
        return None  # Si no hay números positivos, devuelve None
    return sum(positivos) / len(positivos)  # Calcula el promedio de los números positivos

# Ejemplo de uso
lista = [-1, 2, 3, -4, 5]
resultado = promedio_positivos(lista)
if resultado is None:
    print("No hay números positivos.")
else:
    print(f"El promedio de los números positivos es: {resultado:.2f}")
