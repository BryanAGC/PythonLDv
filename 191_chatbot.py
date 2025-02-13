"""
Crea un chatbot básico con respuestas automáticas.
"""
import random

respuestas = {
    "hola": ["¡Hola!", "¡Buen día!", "¡Hola, humano!"],
    "adios": ["Hasta luego", "Nos vemos", "Bye"],
    "como estas": ["Bien, ¿y tú?", "Genial, gracias por preguntar"]
}

def chatbot():
    while True:
        pregunta = input("Tú: ").lower()
        if pregunta in respuestas:
            print("Chatbot:", random.choice(respuestas[pregunta]))
        else:
            print("Chatbot: No entiendo esa pregunta.")

chatbot()
