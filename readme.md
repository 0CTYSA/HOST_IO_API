# README for the Host.io Data Query and Storage Script

This Python script allows you to query the Host.io API and save the results in JSON files organized by domain. It's useful for obtaining and storing detailed information about specific domains by using different endpoints provided by the Host.io API.

## Initial Setup

1. **API Token**: Before running the script, ensure you have a valid Host.io API token. You will need to configure this token in the `api_token` variable within the script.

## Requirements

- Python 3
- `requests` library
- Internet access to make API calls

## Installing Dependencies

To install the necessary dependencies, run the following command:

```bash
pip install requests
```

## Script Structure

- **Authentication**: Uses an API token to authenticate requests. The token is included in the authorization header of each request.
- **Directory Creation**: The script creates a base directory named `results`, where the data for each domain is stored in individual subfolders.
- **Query and Storage Function**: `fetch_and_save_data(domain, endpoint, filename, params=None)` performs the API requests and saves the data in JSON files.

## Using the Script

To use the script, follow these steps:

1. Run the script in your Python environment.
2. Enter up to five domains when prompted in the console. The script will create a folder for each domain and save the data retrieved from the `web`, `related`, and `full` endpoints.
3. You can end the domain entry process early by typing 'done'.

## Query Examples

- **Web Information Query**: Retrieves metadata from the homepage of a domain.
- **Related Domains Query**: Returns information about related domains based on various criteria.
- **Full Query**: Includes combined information from multiple endpoints for a domain.

## Error Handling

The script handles the following types of errors:

- Connection or API errors, reporting the HTTP status code.
- JSON decoding errors if the response is invalid.

## Logs

The script prints the status of operations to the console, including specific errors related to API requests.

This script is a basic yet effective tool for users who need to perform bulk analysis or storage of domain information using the Host.io API. For more details on the endpoints and possible parameters, refer to the [official Host.io documentation](https://host.io/docs).
