import requests
import os
import json

# Configura tu token de API aquí
api_token = 'tu_token_de_api'
headers = {'Authorization': f'Bearer {api_token}'}

# Dominio o IP a analizar
domain = 'ejemplo.com'

# Crear la carpeta principal para los resultados si no existe
base_path = 'resultados'
if not os.path.exists(base_path):
    os.makedirs(base_path)

# Crear una subcarpeta para el dominio específico
domain_path = os.path.join(base_path, domain)
if not os.path.exists(domain_path):
    os.makedirs(domain_path)

# Función para realizar las consultas a la API y guardar los resultados


def fetch_and_save_data(endpoint, filename):
    url = f'https://host.io/api/{endpoint}/{domain}?token={api_token}'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        with open(os.path.join(domain_path, f'{filename}.json'), 'w') as file:
            json.dump(response.json(), file, indent=4)
    else:
        print(f'Error: {response.json().get(
            "error", "Unknown error")} al intentar obtener datos de {endpoint}')


# Obtener y guardar datos
fetch_and_save_data('web', 'web_info')
fetch_and_save_data('dns', 'dns_info')
fetch_and_save_data('related', 'related_info')

print(f"Datos guardados en la carpeta '{domain_path}'")
