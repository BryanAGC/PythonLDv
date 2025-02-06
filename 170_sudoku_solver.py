"""
Resuelve un Sudoku usando el algoritmo de backtracking.
"""
def es_valido(tablero, fila, col, num):
    for i in range(9):
        if tablero[fila][i] == num or tablero[i][col] == num:
            return False
    box_x, box_y = fila // 3 * 3, col // 3 * 3
    for i in range(3):
        for j in range(3):
            if tablero[box_x + i][box_y + j] == num:
                return False
    return True

def resolver_sudoku(tablero):
    for fila in range(9):
        for col in range(9):
            if tablero[fila][col] == 0:
                for num in range(1, 10):
                    if es_valido(tablero, fila, col, num):
                        tablero[fila][col] = num
                        if resolver_sudoku(tablero):
                            return True
                        tablero[fila][col] = 0
                return False
    return True

sudoku = [
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

resolver_sudoku(sudoku)
for fila in sudoku:
    print(fila)
