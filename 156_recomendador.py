"""
Implementa un sistema de recomendación con filtrado colaborativo basado en similitud de coseno.
"""
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

usuarios = {
    "Alice": [5, 3, 4, 4],
    "Bob": [3, 1, 2, 3],
    "Charlie": [4, 3, 4, 5],
    "David": [3, 3, 1, 5]
}

matriz = np.array(list(usuarios.values()))
similitud = cosine_similarity(matriz)

usuarios_lista = list(usuarios.keys())

def recomendar(usuario):
    idx = usuarios_lista.index(usuario)
    sim_scores = similitud[idx]
    recomendacion = np.argmax(np.mean(matriz * sim_scores[:, np.newaxis], axis=0))
    return f"Recomiendo el ítem {recomendacion} para {usuario}"

print(recomendar("Bob"))
