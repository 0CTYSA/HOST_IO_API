# README para el Script de Consulta y Almacenamiento de Datos de Host.io

Este script de Python permite realizar consultas a la API de Host.io y guardar los resultados en archivos JSON organizados por dominios. Es útil para obtener y almacenar información detallada sobre dominios específicos mediante el uso de diferentes endpoints proporcionados por la API de Host.io.

## Configuración Inicial

1. **Token de API**: Antes de ejecutar el script, asegúrate de tener un token válido de API de Host.io. Deberás configurar este token en la variable `api_token` dentro del script.

## Requisitos

- Python 3
- Biblioteca `requests`
- Acceso a Internet para realizar llamadas a la API

## Instalación de Dependencias

Para instalar las dependencias necesarias, ejecuta el siguiente comando:

```bash
pip install requests
```

## Estructura del Script

- **Autenticación**: Utiliza un token de API para autenticar las solicitudes. El token se incluye en el header de autorización de cada solicitud.
- **Creación de Directorios**: El script crea un directorio base llamado `resultados`, donde se almacenan los datos de cada dominio en subcarpetas individuales.
- **Función de Consulta y Almacenamiento**: `fetch_and_save_data(domain, endpoint, filename, params=None)` realiza las solicitudes a la API y guarda los datos en archivos JSON.

## Uso del Script

Para utilizar el script, sigue estos pasos:

1. Ejecuta el script en tu entorno Python.
2. Introduce hasta cinco dominios cuando se soliciten en la consola. El script crea una carpeta para cada dominio y guarda los datos obtenidos de los endpoints: `web`, `related` y `full`.
3. Puedes terminar anticipadamente la introducción de dominios escribiendo 'done'.

## Ejemplos de Consultas

- **Consulta de Información Web**: Obtiene metadatos de la página de inicio de un dominio.
- **Consulta de Dominios Relacionados**: Retorna información sobre dominios relacionados basados en varios criterios.
- **Consulta Completa**: Incluye información combinada de varios endpoints para un dominio.

## Manejo de Errores

El script maneja los siguientes tipos de errores:

- Errores de conexión o de API, reportando el código de estado HTTP.
- Errores de decodificación JSON si la respuesta no es válida.

## Logs

El script imprime en consola los estados de las operaciones, incluyendo errores específicos relacionados con las solicitudes a la API.

Este script es una herramienta básica y efectiva para usuarios que necesitan realizar análisis o almacenamiento masivo de información de dominios utilizando la API de Host.io. Para más detalles sobre los endpoints y los posibles parámetros, consulta la [documentación oficial de Host.io](https://host.io/docs).
