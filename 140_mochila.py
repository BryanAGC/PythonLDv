"""
Resuelve el problema de la mochila con Programación Dinámica.
"""
def mochila(valores, pesos, capacidad):
    n = len(valores)
    dp = [[0] * (capacidad + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacidad + 1):
            if pesos[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], valores[i - 1] + dp[i - 1][w - pesos[i - 1]])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacidad]

# Ejemplo de uso
valores = [60, 100, 120]
pesos = [10, 20, 30]
capacidad = 50
print(mochila(valores, pesos, capacidad))
