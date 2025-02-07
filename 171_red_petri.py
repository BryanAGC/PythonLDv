"""
Simula una red de Petri con transiciones y marcas.
"""
class RedDePetri:
    def __init__(self, plazas, transiciones):
        self.plazas = plazas
        self.transiciones = transiciones

    def disparar(self, transicion):
        if all(self.plazas[plaza] >= req for plaza, req in self.transiciones[transicion]["entrada"].items()):
            for plaza, req in self.transiciones[transicion]["entrada"].items():
                self.plazas[plaza] -= req
            for plaza, prod in self.transiciones[transicion]["salida"].items():
                self.plazas[plaza] += prod
            return True
        return False

plazas = {"P1": 1, "P2": 0, "P3": 0}
transiciones = {
    "T1": {"entrada": {"P1": 1}, "salida": {"P2": 1}},
    "T2": {"entrada": {"P2": 1}, "salida": {"P3": 1}}
}

red = RedDePetri(plazas, transiciones)
print(red.disparar("T1"))  # True
print(red.plazas)
print(red.disparar("T2"))  # True
print(red.plazas)
