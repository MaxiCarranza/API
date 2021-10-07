from os import error
from typing import Counter
from flask import Flask, json, jsonify

app = Flask(__name__)

@app.route('/cotizacion/<string:currency>/<int:quantity>')

def getValidador(currency,quantity):
    Valores = ['EUR','USD','BRL','BGN']
    monedasFound = [x for x in Valores if Valores[0] == currency or Valores[1] == currency or Valores[2] == currency or Valores[2] == currency]
    if (len(monedasFound) == 0):
        return jsonify({"message": "Product not found 404 "})
    elif (quantity <= 0):
        return jsonify({"message": "Product not found 404 "})
    else:
        return jsonify({"Moneda": currency, "Cantidad" : quantity })
        
        
if __name__ == '__main__':
    URL = 'http://localhost:4000/cotizacion/{currency}/{quantity}'
    print(f'API creada: {URL} Ingresar datos a cotizar.')
    app.run(debug=True, port=4000)