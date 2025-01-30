"""
Implementa el algoritmo de la Mochila 0/1 para maximizar el valor total de objetos seleccionados sin exceder la capacidad.
"""
def mochila(capacidad, pesos, valores, n):
    dp = [[0] * (capacidad + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacidad + 1):
            if pesos[i - 1] <= w:
                dp[i][w] = max(valores[i - 1] + dp[i - 1][w - pesos[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacidad]

valores = [60, 100, 120]
pesos = [10, 20, 30]
capacidad = 50
print(mochila(capacidad, pesos, valores, len(valores)))  # 220
