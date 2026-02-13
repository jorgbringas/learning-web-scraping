import requests
from bs4 import BeautifulSoup

# Prueba de extracción de resultados en el motor de búsqueda de Google.
url = "https://www.google.com/"

# Configuración de User-Agent oficial para evitar bloqueos por peticiones automatizadas.
cabeceras = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/119.0.0.0 Safari/537.36"
}
mis_parametros = {"q": "como cocinar quinoa"}
mis_cooks = {}

# Envío de la petición HTTP con parámetros de búsqueda y cabeceras personalizadas.
respuesta = requests.get(url, params=mis_parametros, headers=cabeceras, timeout=10, cookies=mis_cooks)

# Análisis sintáctico del contenido HTML mediante BeautifulSoup.
sopa = BeautifulSoup(respuesta.text, 'html.parser')

# Extracción del título de la página de resultados.
print(f"El título de la web es: {sopa.title.string}")





