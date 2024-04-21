import requests
import os
import json

# Configura tu token de API
api_token = 'tu_token_de_api'
headers = {'Authorization': f'Bearer {api_token}'}

# Dominio a analizar
domain = 'ejemplo.com'

# Base path para los resultados
base_path = 'resultados'

# Path específico para el dominio
domain_path = os.path.join(base_path, domain)
if not os.path.exists(domain_path):
    os.makedirs(domain_path)

# Función para realizar las consultas a la API y guardar los datos


def fetch_and_save_data(endpoint, params, filename):
    url = f'https://host.io/api/{endpoint}'
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        # Crea o sobrescribe el archivo JSON con los resultados
        with open(os.path.join(domain_path, f'{filename}.json'), 'w') as file:
            json.dump(response.json(), file, indent=4)
        return response.json()
    else:
        # Manejo de errores
        error = response.json().get('error', 'Error desconocido')
        print(f'Error al obtener datos para {endpoint}: {error}')
        return None


# Obtener información del DNS para extraer la IP
dns_info = fetch_and_save_data('dns', {'domain': domain}, 'dns_info')

# Si se obtuvo la información del DNS correctamente, extraer la IP y buscar co-hosted
if dns_info and 'a' in dns_info:
    # Asumimos la primera entrada A como la IP del dominio
    ip_address = dns_info['a'][0]
    fetch_and_save_data('domains/ip', {'ip': ip_address}, 'cohosted_domains')

# Los demás llamados permanecen iguales
fetch_and_save_data('web', {'domain': domain}, 'web_info')
fetch_and_save_data('related', {'domain': domain}, 'related_info')
fetch_and_save_data('full', {'domain': domain}, 'full_info')

# Imprimir la ruta donde se guardaron los datos
print(f"Datos guardados en la carpeta '{domain_path}'")
