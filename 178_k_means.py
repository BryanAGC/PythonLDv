"""
Implementa el algoritmo K-Means desde cero para agrupar datos.
"""
import numpy as np

def k_means(datos, k, iteraciones=100):
    centroides = datos[np.random.choice(datos.shape[0], k, replace=False)]
    
    for _ in range(iteraciones):
        etiquetas = np.array([np.argmin([np.linalg.norm(x - c) for c in centroides]) for x in datos])
        nuevos_centroides = np.array([datos[etiquetas == i].mean(axis=0) for i in range(k)])
        
        if np.all(centroides == nuevos_centroides):
            break
        centroides = nuevos_centroides

    return etiquetas, centroides

datos = np.array([[1,2], [1,3], [4,5], [7,8], [8,9]])
etiquetas, centroides = k_means(datos, 2)
print(centroides)
