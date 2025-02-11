"""
Extrae los títulos de los artículos de una página web usando BeautifulSoup.
"""
import requests
from bs4 import BeautifulSoup

def obtener_titulos(url):
    respuesta = requests.get(url)
    sopa = BeautifulSoup(respuesta.text, "html.parser")
    titulos = [t.text for t in sopa.find_all("h2")]
    return titulos

# print(obtener_titulos("https://example.com"))  # Descomentar para probar con una web real
