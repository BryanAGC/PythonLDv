"""
Genera una caminata aleatoria en 2D y gráficala.
"""
import numpy as np
import matplotlib.pyplot as plt

posiciones = np.zeros((100, 2))
for i in range(1, 100):
    posiciones[i] = posiciones[i-1] + np.random.choice([-1, 1], size=2)

plt.plot(posiciones[:, 0], posiciones[:, 1])
plt.show()
