"""
Identificación y extracción de elementos estructurales específicos.
"""
import requests
from bs4 import BeautifulSoup

# URL de destino para la práctica de extracción de texto y etiquetas.
url = "https://www.paulinacocina.net/como-cocinar-quinoa/27793"

# Definición de cabeceras para la identificación de la sesión del navegador.
cabeceras = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/119.0.0.0 Safari/537.36"
}
mis_parametros = {"q": "como cocinar quinoa"}
mis_cooks = {}

# Captura del contenido íntegro del sitio web.
respuesta = requests.get(url, params=mis_parametros, headers=cabeceras, timeout=10, cookies=mis_cooks)

# Procesamiento del DOM mediante BeautifulSoup.
sopa = BeautifulSoup(respuesta.text, 'html.parser')

# Recuperación de la totalidad del texto presente en la página.
print(f"El contenido completo de la web es: {sopa.get_text()}")


"""
--- Método 2: Extracción de encabezados H3 ---
"""

# Localización de todos los elementos h3 presentes en el documento.
enlaces = sopa.find_all('h3')

# Recorrido y visualización sistemática de cada encabezado identificado.
for h3 in enlaces:
    print(f"He encontrado este título: {h3.string}")


"""
--- Método 3: Listado de hipervínculos (etiquetas a) ---
"""
# Selección de todos los elementos de enlace en la estructura HTML.
links = sopa.find_all('a')

for link in links:
    # Obtención del texto descriptivo del enlace.
    texto = link.string 
    # Extracción de la dirección URL del atributo href.
    url_destino = link.get('href')
    print(f"Texto: {texto} | Link: {url_destino}")