"""
Escribe una función que reciba una lista de números y devuelva la suma de todos los números, excluyendo el mayor y el menor.
"""
def suma_excluyendo_extremos(lista):
    if len(lista) <= 2:
        return 0
    mayor = max(lista)
    menor = min(lista)
    return sum(lista) - mayor - menor

# Ejemplo de uso
lista = [1, 2, 3, 4, 5]
resultado = suma_excluyendo_extremos(lista)
print(f"La suma excluyendo el mayor y el menor es: {resultado}")
