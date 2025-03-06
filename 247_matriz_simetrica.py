def es_matriz_simetrica(matriz):
    n = len(matriz)
    for i in range(n):
        for j in range(n):
            if matriz[i][j] != matriz[j][i]:
                return False
    return True

matriz_simetrica = [[1, 2, 3], [2, 4, 5], [3, 5, 6]]
print(es_matriz_simetrica(matriz_simetrica))  
