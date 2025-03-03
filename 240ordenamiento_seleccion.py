def ordenamiento_seleccion(lista):
    for i in range(len(lista)):
        min_idx = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]

numeros = [64, 25, 12, 22, 11]
ordenamiento_seleccion(numeros)
print(numeros)  
