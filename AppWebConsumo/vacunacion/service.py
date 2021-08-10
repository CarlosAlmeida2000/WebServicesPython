import requests
import json

def generate_request(url, params={}):
    headers = {'content-type': 'application/json'}
    response = requests.post(url, data=json.dumps(params),headers=headers)
    if response.status_code == 200:
        return response.json()

def get_LgVacun(params={}):
    respuesta = generate_request('http://127.0.0.1:8000/api-vacunacion/consultar-lugar/', params)
    print(respuesta)
    if respuesta:
       resultJSON = respuesta.get('consulta')
       return resultJSON
    return ""