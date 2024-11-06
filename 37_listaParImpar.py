"""
Escribe una función que reciba una lista de números y devuelva una nueva lista 
donde cada número es reemplazado por "par" si es par y por "impar" si es impar.


"""

def reemplazar_par_impar(lista_numeros):
    return ["par" if numero % 2 == 0 else "impar" for numero in lista_numeros]

# Ejemplo de uso
lista = [1, 2, 3, 4, 5]
resultado = reemplazar_par_impar(lista)
print(f"Lista con 'par' e 'impar': {resultado}")
