"""
Simula una Máquina de Turing simple con reglas predefinidas.
"""
class MaquinaTuring:
    def __init__(self, cinta, estado_inicial, reglas):
        self.cinta = list(cinta)
        self.posicion = 0
        self.estado = estado_inicial
        self.reglas = reglas

    def ejecutar(self):
        while (self.estado, self.cinta[self.posicion]) in self.reglas:
            nuevo_estado, nuevo_simbolo, movimiento = self.reglas[(self.estado, self.cinta[self.posicion])]
            self.cinta[self.posicion] = nuevo_simbolo
            self.estado = nuevo_estado
            self.posicion += 1 if movimiento == "R" else -1

        return "".join(self.cinta)

cinta_inicial = "1101_"
reglas = {
    ('q0', '1'): ('q0', '1', 'R'),
    ('q0', '0'): ('q0', '0', 'R'),
    ('q0', '_'): ('q1', '1', 'R')
}

turing = MaquinaTuring(cinta_inicial, 'q0', reglas)
print(turing.ejecutar())  # 11011
