"""
Crea un servidor web simple con Flask.
"""
from flask import Flask

app = Flask(__name__)

@app.route('/')
def inicio():
    return "¡Hola desde Flask!"

if __name__ == '__main__':
    app.run(debug=True)
