import requests
import json

def generate_request(url, params={}):
    response = requests.post(url, params=params)

    if response.status_code == 200:
        return response.json()

def get_LgVacun(params={}):
    respuesta = generate_request('http://127.0.0.1:8000/api-vacunacion/consultar-lugar/', params)
    print(respuesta)
    if respuesta:
       resultJSON = respuesta.get('consulta')
       return resultJSON
    return ""