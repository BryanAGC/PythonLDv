"""
Compara dos textos y calcula su similitud usando NLP.
"""
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def similitud(texto1, texto2):
    vectorizador = TfidfVectorizer()
    vectores = vectorizador.fit_transform([texto1, texto2])
    return cosine_similarity(vectores[0], vectores[1])[0][0]

texto1 = "Este es un documento importante sobre aprendizaje automático."
texto2 = "Aprendizaje automático es importante en este documento."

print("Similitud:", similitud(texto1, texto2))
