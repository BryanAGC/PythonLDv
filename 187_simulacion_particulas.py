"""
Simula el movimiento de partículas en un espacio bidimensional.
"""
import numpy as np
import matplotlib.pyplot as plt

class Particula:
    def __init__(self, x, y, vx, vy):
        self.x, self.y = x, y
        self.vx, self.vy = vx, vy

    def mover(self):
        self.x += self.vx
        self.y += self.vy

particulas = [Particula(np.random.rand()*10, np.random.rand()*10, np.random.rand()-0.5, np.random.rand()-0.5) for _ in range(50)]
for _ in range(100):
    plt.clf()
    for p in particulas:
        p.mover()
        plt.scatter(p.x, p.y)
    plt.pause(0.05)
