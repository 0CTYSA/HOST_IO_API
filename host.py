import requests
import os
import json

# Configure your API token here
api_token = 'key'
headers = {'Authorization': f'Bearer {api_token}'}

# Create the main folder for the results if it does not exist
base_path = 'resultados'
if not os.path.exists(base_path):
    os.makedirs(base_path)

# Function to perform the API queries and save the results


def fetch_and_save_data(domain, endpoint, filename, params=None):
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
                  response.text} when trying to obtain data from {endpoint}')
    except json.JSONDecodeError:
        print(
            f'Error: JSON could not be decoded in the response from {endpoint}')


# Request domains from the console
for i in range(5):
    domain = input(f"Enter the domain {
                   i+1} of 5 or type 'done' to finish: ")
    if domain.lower() == 'done':
        break

    # Create a subfolder for the specific domain
    domain_path = os.path.join(base_path, domain)
    if not os.path.exists(domain_path):
        os.makedirs(domain_path)

    # Execute query function and save data
    fetch_and_save_data(domain, 'web', 'web_info')
    fetch_and_save_data(domain, 'related', 'related_info')
    fetch_and_save_data(domain, 'full', 'full_info')

    print(f"Data stored in the folder '{domain_path}'")

print("Process completed for all domains.")
