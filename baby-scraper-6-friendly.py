import requests
from bs4 import BeautifulSoup

# Sitio web diseñado específicamente para la práctica de web scraping.
url = "http://quotes.toscrape.com/"

# Realización de la petición GET (el sitio es permisivo con los bots).
respuesta = requests.get(url)

# Análisis del HTML con BeautifulSoup.
sopa = BeautifulSoup(respuesta.text, 'html.parser')

# Localización de citas y sus autores mediante clases CSS específicas.
citas = sopa.find_all('span', class_='text')
autores = sopa.find_all('small', class_='author')

print("\n--- CITAS FAMOSAS ENCONTRADAS ---\n")

# Asociación e impresión de cada cita con su autor correspondiente.
for i in range(len(citas)):
    print(f"Cita: {citas[i].get_text()}")
    print(f"Autor: {autores[i].get_text()}")
    print("-" * 40)