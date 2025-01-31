"""
Calcula la longitud de la subsecuencia común más larga entre dos cadenas con programación dinámica.
"""
def lcs(x, y):
    m, n = len(x), len(y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]

cadena1 = "AGGTAB"
cadena2 = "GXTXAYB"
print(lcs(cadena1, cadena2))  # 4
