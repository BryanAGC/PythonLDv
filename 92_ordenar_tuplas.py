"""
Dada una lista de tuplas, ordena primero por el segundo elemento de forma ascendente 
y luego por el primer elemento de forma descendente.
"""
def ordenar_tuplas(lista):
    return sorted(lista, key=lambda x: (x[1], -x[0]))
tuplas = [(5, 2), (3, 1), (6, 2), (1, 3)]
print(ordenar_tuplas(tuplas))  
