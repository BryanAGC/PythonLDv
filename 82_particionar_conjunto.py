"""
Dado un conjunto de números, determina si se puede dividir en dos subconjuntos con la misma suma.
"""
def puede_particionar(nums):
    total = sum(nums)
    if total % 2 != 0:
        return False
    objetivo = total // 2
    dp = [False] * (objetivo + 1)
    dp[0] = True

    for num in nums:
        for j in range(objetivo, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]

    return dp[objetivo]

# Ejemplo de uso
nums = [1, 5, 11, 5]
print(puede_particionar(nums))  # True
