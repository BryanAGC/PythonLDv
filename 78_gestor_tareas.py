"""
Crea una clase para gestionar tareas con prioridad. Debe permitir añadir tareas, marcar tareas como completadas 
y mostrar las tareas pendientes en orden de prioridad.
"""
import heapq

class GestorTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, descripcion, prioridad):
        heapq.heappush(self.tareas, (prioridad, descripcion))

    def completar_tarea(self):
        if self.tareas:
            return heapq.heappop(self.tareas)[1]
        return "No hay tareas pendientes."

    def mostrar_tareas(self):
        return sorted(self.tareas)

# Ejemplo de uso
gestor = GestorTareas()
gestor.agregar_tarea("Hacer ejercicio", 2)
gestor.agregar_tarea("Terminar proyecto", 1)
gestor.agregar_tarea("Leer un libro", 3)
print(gestor.mostrar_tareas())  # [(1, 'Terminar proyecto'), (2, 'Hacer ejercicio'), (3, 'Leer un libro')]
print(gestor.completar_tarea())  # "Terminar proyecto"
