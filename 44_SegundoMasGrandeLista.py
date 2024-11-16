"""
Escribe una función que reciba una lista de
números y devuelva el segundo número más grande 
de la lista.
"""
def segundo_mayor(lista_numeros):
    if len(lista_numeros) < 2:
        return None  # No hay suficientes números para encontrar un segundo mayor
    
    # Elimina duplicados y ordena la lista en orden descendente
    lista_unica = list(set(lista_numeros))
    lista_unica.sort(reverse=True)
    
    if len(lista_unica) < 2:
        return None  # Todos los números son iguales
    
    return lista_unica[1]  # Retorna el segundo mayor

# Ejemplo de uso
lista = [10, 20, 30, 40, 50]
resultado = segundo_mayor(lista)
print(f"El segundo número más grande es: {resultado}")
