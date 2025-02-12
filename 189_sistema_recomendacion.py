"""
Implementa un sistema de recomendación basado en similitud de coseno.
"""
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

usuarios = np.array([[5, 3, 0, 1], [4, 0, 0, 1], [1, 1, 0, 5], [0, 1, 5, 4]])
similitudes = cosine_similarity(usuarios)

print("Matriz de similitud entre usuarios:\n", similitudes)
