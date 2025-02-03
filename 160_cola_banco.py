"""
Simula la atención en un banco usando una cola de prioridad donde los clientes VIP tienen prioridad.
"""
import heapq

class Cliente:
    def __init__(self, nombre, prioridad):
        self.nombre = nombre
        self.prioridad = prioridad

    def __lt__(self, otro):
        return self.prioridad < otro.prioridad

cola = []
heapq.heappush(cola, Cliente("Carlos", 2))
heapq.heappush(cola, Cliente("Ana", 1))  # Cliente VIP
heapq.heappush(cola, Cliente("Luis", 3))

while cola:
    cliente = heapq.heappop(cola)
    print(f"Atendiendo a: {cliente.nombre}")
