import requests
import json

with open ('config.json') as config_file:
    config = json.load(config_file)

headers = {
    'APIKey' : config['client_key'],
    'ChaveCliente' : config['client']
}

def api_consult(start_date, finish_date):
    url = f"http://webapigenial.genialnet.com.br:7000/genial/IntegracaoMde/v1/get?DataInicial={start_date}&DataFinal={finish_date}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None
