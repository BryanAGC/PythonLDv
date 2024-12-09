"""
Dado un mapa representado como una matriz donde 1 representa tierra y 0 representa agua, 
calcula cuántas islas (regiones de tierra conectadas horizontal o verticalmente) hay en el mapa.
"""
def contar_islas(mapa):
    def dfs(i, j):
        if i < 0 or j < 0 or i >= len(mapa) or j >= len(mapa[0]) or mapa[i][j] == 0:
            return
        mapa[i][j] = 0
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)

    islas = 0
    for i in range(len(mapa)):
        for j in range(len(mapa[0])):
            if mapa[i][j] == 1:
                islas += 1
                dfs(i, j)
    return islas

mapa = [
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1]
]
print(contar_islas(mapa))  # 3
