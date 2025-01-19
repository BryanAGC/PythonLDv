"""
Detecta si una lista enlazada tiene un ciclo usando el algoritmo de Floyd.
"""
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

def tiene_ciclo(nodo):
    lento, rapido = nodo, nodo
    while rapido and rapido.siguiente:
        lento = lento.siguiente
        rapido = rapido.siguiente.siguiente
        if lento == rapido:
            return True
    return False

# Ejemplo de uso
nodo1, nodo2, nodo3 = Nodo(1), Nodo(2), Nodo(3)
nodo1.siguiente, nodo2.siguiente, nodo3.siguiente = nodo2, nodo3, nodo1  # Ciclo
print(tiene_ciclo(nodo1))  # True
