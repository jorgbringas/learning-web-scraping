import requests
from bs4 import BeautifulSoup

# URL del sitio web para la prueba de conexión inicial.
url = "https://peru21.pe/"

# Ejecución de la petición GET para recuperar el contenido de la página.
respuesta = requests.get(url)

# Extracción y estructuración del HTML mediante BeautifulSoup.
# Esto permite la identificación de etiquetas semánticas como títulos o encabezados.
sopa = BeautifulSoup(respuesta.text, 'html.parser')

# Obtención del título del documento para confirmar que la extracción es funcional.
titulo = sopa.title.string

# Impresión del resultado en la terminal.
print(f"El título de la web es: {titulo}")