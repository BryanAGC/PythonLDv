"""
Dada una lista que puede contener duplicados, genera todos los subconjuntos únicos.
"""
def subconjuntos_unicos(nums):
    nums.sort()
    resultado = []
    def backtrack(indice, camino):
        resultado.append(camino[:])
        for i in range(indice, len(nums)):
            if i > indice and nums[i] == nums[i - 1]:
                continue
            camino.append(nums[i])
            backtrack(i + 1, camino)
            camino.pop()
    backtrack(0, [])
    return resultado

nums = [1, 2, 2]
print(subconjuntos_unicos(nums))  # [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
