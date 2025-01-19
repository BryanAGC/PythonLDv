"""
Dado un conjunto de objetos con pesos y valores, y una mochila con un límite de peso, 
encuentra la mejor combinación de objetos para maximizar el valor total sin exceder el límite.
"""
def mochila(pesos, valores, capacidad):
    n = len(valores)
    dp = [[0] * (capacidad + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(capacidad + 1):
            if pesos[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - pesos[i - 1]] + valores[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[n][capacidad]

# Ejemplo de uso
print(mochila([2, 3, 4, 5], [3, 4, 5, 6], 5))  # 7
