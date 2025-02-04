"""
Implementa una red neuronal de una sola capa con activación sigmoide usando NumPy.
"""
import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def red_neuronal(entradas, pesos):
    return sigmoid(np.dot(entradas, pesos))

entradas = np.array([0.5, 0.8])
pesos = np.array([0.2, 0.6])

salida = red_neuronal(entradas, pesos)
print(salida)
