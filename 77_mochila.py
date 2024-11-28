"""
Implementa la solución del problema de la mochila utilizando programación dinámica.
"""
def mochila(pesos, valores, capacidad):
    n = len(valores)
    dp = [[0] * (capacidad + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(1, capacidad + 1):
            if pesos[i - 1] <= w:
                dp[i][w] = max(valores[i - 1] + dp[i - 1][w - pesos[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[n][capacidad]

# Ejemplo de uso
pesos = [1, 2, 3]
valores = [10, 15, 40]
capacidad = 5
print(mochila(pesos, valores, capacidad))  # 55
