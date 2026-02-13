import requests
from bs4 import BeautifulSoup

# --- BABY SCRAPER 4: Implementación de búsqueda en DuckDuckGo (HTML) ---

# Selección del endpoint estático de DuckDuckGo para facilitar el acceso a los datos.
url = "https://html.duckduckgo.com/html/"

# Parámetros técnicos de la cabecera HTTP.
cabeceras = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/119.0.0.0 Safari/537.36"
}

# Configuración de los términos de búsqueda.
mis_parametros = {"q": "como cocinar quinoa"}

# Ejecución de la consulta web y recuperación de la respuesta del servidor.
print(f"Buscando '{mis_parametros['q']}' en DuckDuckGo...")
respuesta = requests.get(url, params=mis_parametros, headers=cabeceras, timeout=10)

# Parsing y estructuración del contenido web mediante BeautifulSoup.
sopa = BeautifulSoup(respuesta.text, 'html.parser')

# Localización de todos los nodos de hipervínculo en el documento procesado.
enlaces = sopa.find_all('a')

print("\n--- RESULTADOS ENCONTRADOS ---\n")

for link in enlaces:
    # Captura del texto contenido en el elemento.
    texto = link.get_text().strip()
    
    # Recuperación de la dirección de destino almacenada en el atributo href.
    url_destino = link.get('href')
    
    # Filtrado lógico para omitir elementos de navegación sin contenido textual.
    if texto:
        print(f"TÍTULO: {texto}")
        print(f"LINK:   {url_destino}")
        print("-" * 30)