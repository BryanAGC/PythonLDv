"""
Implementa el algoritmo de K-Means para agrupar puntos en 2D.
"""
import numpy as np
from sklearn.cluster import KMeans

datos = np.array([[1, 2], [2, 3], [3, 4], [8, 7], [9, 6], [10, 8]])
kmeans = KMeans(n_clusters=2, random_state=0).fit(datos)
print(kmeans.labels_)
