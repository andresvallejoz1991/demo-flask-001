"""
Introducción a Flask
https://parzibyte.me/blog
"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def inicio():
    return "<h1>Introducción a Flask</h1><h2>@andresvallejoz1991</h2>"

@app.route('/suma')
def suma():
    resultado = 10 + 10
    return "<h2>El resultado de la Suma es:</h2><h3>10 + 10 = %d</h3>" % (resultado)

@app.route('/listado')
def listado():
	return "<h2>Provincias</h2><ul><li>Quito</li><li>Loja</li><li>Azuay</li><li>Ambato</li><li>Riobamba</li><li>Cotopaxi</li><li>Latacunga</li></ul>"


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000, debug=True)
