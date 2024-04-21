import requests
import os
import json

# Configura tu token de API aquí
api_token = 'tu_token_de_api'
headers = {'Authorization': f'Bearer {api_token}'}

# Dominio o IP a analizar
domain = 'ejemplo.com'

# Crea la carpeta para los resultados si no existe
if not os.path.exists('resultados'):
    os.makedirs('resultados')

# Función para realizar las consultas a la API y guardar los resultados


def fetch_and_save_data(endpoint, filename):
    url = f'https://host.io/api/{endpoint}/{domain}?token={api_token}'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        with open(f'resultados/{filename}.json', 'w') as file:
            json.dump(response.json(), file, indent=4)
    else:
        print(f'Error: {response.json()[
              "error"]} al intentar obtener datos de {endpoint}')


# Obtener y guardar datos
fetch_and_save_data('web', 'web_info')
fetch_and_save_data('dns', 'dns_info')
fetch_and_save_data('related', 'related_info')

print("Datos guardados en la carpeta 'resultados'")
