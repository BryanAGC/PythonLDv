"""
Escribe una función que reciba un tablero de Sudoku (9x9) como una lista de listas 
y valide si cumple las reglas básicas del Sudoku (filas, columnas y subcuadrículas deben contener números únicos del 1 al 9).
"""
def es_sudoku_valido(tablero):
    def es_valido_grupo(grupo):
        numeros = [num for num in grupo if num != 0]
        return len(numeros) == len(set(numeros))
    
    def obtener_subcuadrícula(tablero, fila, col):
        return [tablero[r][c] for r in range(fila, fila + 3) for c in range(col, col + 3)]

    for i in range(9):
        if not es_valido_grupo(tablero[i]) or not es_valido_grupo([fila[i] for fila in tablero]):
            return False

    for fila in range(0, 9, 3):
        for col in range(0, 9, 3):
            if not es_valido_grupo(obtener_subcuadrícula(tablero, fila, col)):
                return False
    
    return True

tablero = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
print(es_sudoku_valido(tablero))  # True (es válido hasta ahora)
