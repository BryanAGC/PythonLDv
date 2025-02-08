"""
Crea un sistema de recomendación usando filtrado colaborativo basado en usuarios.
"""
import numpy as np

def similitud_coseno(usuario1, usuario2):
    return np.dot(usuario1, usuario2) / (np.linalg.norm(usuario1) * np.linalg.norm(usuario2))

def recomendar(usuario_objetivo, usuarios, productos):
    similitudes = {usuario: similitud_coseno(usuarios[usuario_objetivo], rating) for usuario, rating in usuarios.items() if usuario != usuario_objetivo}
    usuario_similar = max(similitudes, key=similitudes.get)
    
    recomendaciones = [(producto, rating) for producto, rating in enumerate(usuarios[usuario_similar]) if usuarios[usuario_objetivo][producto] == 0]
    recomendaciones.sort(key=lambda x: -x[1])
    return [productos[i[0]] for i in recomendaciones]

productos = ["Libro A", "Libro B", "Libro C", "Libro D"]
usuarios = {
    "Juan": [5, 0, 3, 0],
    "Ana": [4, 5, 0, 3],
    "Carlos": [0, 3, 4, 5]
}

print(recomendar("Juan", usuarios, productos))
