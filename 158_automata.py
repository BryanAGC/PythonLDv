"""
Construye un autómata finito determinista (AFD) que reconoce cadenas que terminan en 'ab'.
"""
class AutomataFinito:
    def __init__(self):
        self.estado = "q0"
        self.transiciones = {
            "q0": {"a": "q1", "b": "q0"},
            "q1": {"a": "q1", "b": "q2"},
            "q2": {"a": "q1", "b": "q0"}
        }
        self.estado_final = "q2"

    def procesar(self, cadena):
        for simbolo in cadena:
            if simbolo in self.transiciones[self.estado]:
                self.estado = self.transiciones[self.estado][simbolo]
            else:
                return False
        return self.estado == self.estado_final

automata = AutomataFinito()
print(automata.procesar("aab"))  # False
print(automata.procesar("ab"))   # True
print(automata.procesar("aaaab"))  # True
