"""
Dado un laberinto representado como una matriz donde 0 es un espacio libre y 1 es un obstáculo, 
encuentra el número de formas de llegar a la esquina inferior derecha desde la superior izquierda.
"""
def caminos_con_obstaculos(matriz):
    filas, columnas = len(matriz), len(matriz[0])
    if matriz[0][0] == 1 or matriz[-1][-1] == 1:
        return 0

    dp = [[0] * columnas for _ in range(filas)]
    dp[0][0] = 1

    for i in range(filas):
        for j in range(columnas):
            if matriz[i][j] == 1:
                dp[i][j] = 0
            else:
                if i > 0:
                    dp[i][j] += dp[i - 1][j]
                if j > 0:
                    dp[i][j] += dp[i][j - 1]
    return dp[-1][-1]
matriz = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]
print(caminos_con_obstaculos(matriz))  # 2
  