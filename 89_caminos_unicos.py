"""
Dada una matriz de tamaño `m x n`, encuentra cuántos caminos únicos existen para ir de la esquina superior izquierda a la esquina inferior derecha.
Solo puedes moverte hacia abajo o hacia la derecha.
"""
def caminos_unicos(m, n):
    dp = [[1] * n for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[-1][-1]

m, n = 3, 7
print(caminos_unicos(m, n))  # 28
