import requests
from bs4 import BeautifulSoup

# --- BABY SCRAPER 5: Extracción de información textual en Wikipedia ---

# URL de destino seleccionada por su arquitectura HTML predecible.
url = "https://es.wikipedia.org/wiki/Quinoa"

# Definición de cabeceras de usuario.
cabeceras = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/119.0.0.0 Safari/537.36"
}

# Petición HTTP y recuperación de los datos del artículo.
print(f"Leyendo sobre la Quinoa en Wikipedia...")
respuesta = requests.get(url, headers=cabeceras, timeout=10)

# Análisis y estructuración de los datos recibidos.
sopa = BeautifulSoup(respuesta.text, 'html.parser')

# Identificación y captura de todas las etiquetas de párrafo (<p>).
parrafos = sopa.find_all('p')

print("\n--- CONTENIDO ENCONTRADO ---\n")

# Restricción del flujo de salida a los primeros tres fragmentos de texto.
for p in parrafos[:3]:
    texto = p.get_text().strip()
    if texto: 
        print(texto)
        print("-" * 50)