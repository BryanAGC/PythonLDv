"""
Escribe una función que reciba una lista de 
números y devuelva una nueva lista con solo los 
números que sean múltiplos de 3.
"""
def multiplos_de_tres(lista_numeros):
    return [num for num in lista_numeros if num % 3 == 0]  # Filtra los números divisibles por 3

# Ejemplo de uso
lista = [1, 3, 4, 9, 10, 12, 15]
resultado = multiplos_de_tres(lista)
print(f"Números múltiplos de 3: {resultado}")
