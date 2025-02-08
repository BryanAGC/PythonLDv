"""
Implementa un modelo Naive Bayes para análisis de sentimiento de textos.
"""
from collections import defaultdict
import math

class NaiveBayes:
    def __init__(self):
        self.palabras_clase = defaultdict(lambda: defaultdict(int))
        self.total_clases = defaultdict(int)
        self.vocabulario = set()

    def entrenar(self, datos):
        for texto, clase in datos:
            self.total_clases[clase] += 1
            for palabra in texto.split():
                self.palabras_clase[clase][palabra] += 1
                self.vocabulario.add(palabra)

    def predecir(self, texto):
        puntajes = {}
        for clase in self.total_clases:
            log_prob = math.log(self.total_clases[clase] / sum(self.total_clases.values()))
            for palabra in texto.split():
                prob = (self.palabras_clase[clase].get(palabra, 0) + 1) / (sum(self.palabras_clase[clase].values()) + len(self.vocabulario))
                log_prob += math.log(prob)
            puntajes[clase] = log_prob
        return max(puntajes, key=puntajes.get)

datos = [
    ("me encanta este producto", "positivo"),
    ("odio este servicio", "negativo"),
    ("es excelente y funciona bien", "positivo"),
    ("terrible, no lo recomiendo", "negativo")
]

modelo = NaiveBayes()
modelo.entrenar(datos)
print(modelo.predecir("es un buen producto"))
