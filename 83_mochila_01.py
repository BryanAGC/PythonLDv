"""
Dado un conjunto de elementos, cada uno con un peso y un valor, 
encuentra el valor máximo que se puede obtener en una mochila con capacidad limitada.
"""
def mochila_01(pesos, valores, capacidad):
    n = len(valores)
    dp = [[0] * (capacidad + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(capacidad + 1):
            if pesos[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - pesos[i - 1]] + valores[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[n][capacidad]

pesos = [1, 2, 3]
valores = [60, 100, 120]
capacidad = 5
print(mochila_01(pesos, valores, capacidad))  # 220
