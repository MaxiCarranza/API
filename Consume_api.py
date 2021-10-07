import requests
import json

TOKEN = "11120|hXDogdpBKpz^7FgLmO7T2PyNXppcAVXM"

if __name__ == "_main_":
    headers ={
        "Accept" : "application/json",
        "Content-Type" : "application/json"
        }
    r = requests.get("https://api.cambio.today/v1/quotes/EUR/USD/json?quantity=1&key=11120|hXDogdpBKpz^7FgLmO7T2PyNXppcAVXM", headers = headers)
    print(f'Moneda',r.json()['result']['target'],'\n'
           'Cantidad',r.json()['result']['quantity'])
    