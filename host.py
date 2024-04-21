import requests
import os
import json

# Configura tu token de API aquí
api_token = 'key'
headers = {'Authorization': f'Bearer {api_token}'}

# Dominio a analizar
domain = 'domain'

# Crear la carpeta principal para los resultados si no existe
base_path = 'resultados'
if not os.path.exists(base_path):
    os.makedirs(base_path)

# Crear una subcarpeta para el dominio específico
domain_path = os.path.join(base_path, domain)
if not os.path.exists(domain_path):
    os.makedirs(domain_path)

# Función para realizar las consultas a la API y guardar los resultados


def fetch_and_save_data(endpoint, filename, params=None):
    url = f'https://host.io/api/{endpoint}/{domain}?token={api_token}'
    if params:
        url += '&' + \
            '&'.join([f'{key}={value}' for key, value in params.items()])
    response = requests.get(url, headers=headers)
    try:
        if response.status_code == 200:
            data = response.json()
            with open(os.path.join(domain_path, f'{filename}.json'), 'w') as file:
                json.dump(data, file, indent=4)
        else:
            print(f'Error {response.status_code}: {
                  response.text} al intentar obtener datos de {endpoint}')
    except json.JSONDecodeError:
        print(
            f'Error: No se pudo decodificar JSON en la respuesta de {endpoint}')


# Ejecutar la función de consulta y guardar datos
fetch_and_save_data('web', 'web_info')
fetch_and_save_data('related', 'related_info')
fetch_and_save_data('full', 'full_info')

print(f"Datos guardados en la carpeta '{domain_path}'")
