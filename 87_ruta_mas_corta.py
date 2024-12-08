"""
Encuentra la ruta más corta desde la esquina superior izquierda hasta la esquina inferior derecha de una matriz de enteros.
Solo puedes moverte hacia la derecha o hacia abajo.
"""
def ruta_mas_corta(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    dp = [[float('inf')] * columnas for _ in range(filas)]
    dp[0][0] = matriz[0][0]
    for i in range(filas):
        for j in range(columnas):
            if i > 0:
                dp[i][j] = min(dp[i][j], dp[i - 1][j] + matriz[i][j])
            if j > 0:
                dp[i][j] = min(dp[i][j], dp[i][j - 1] + matriz[i][j])
    return dp[-1][-1]


matriz = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]
print(ruta_mas_corta(matriz))  # 7
