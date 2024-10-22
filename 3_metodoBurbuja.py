"""
ORDENA UNA LISTA CON ALGORITMO BURBUJA
"""

def bubble_sort(lista):
    for i in range(len(lista)):      
        for j in range(0, len(lista)-i-1):  # Cambié 'len(lista)-1-i' a 'len(lista)-i-1'
            if lista[j] > lista[j+1]:
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux

mi_lista = [1, 3, 2, 14, 143, 39, 0]
bubble_sort(mi_lista)
print(mi_lista)

