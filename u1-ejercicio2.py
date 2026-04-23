import requests
from bs4 import BeautifulSoup

# Definimos la URL de la que deseamos extraer las noticias
url = "https://news.ycombinator.com/"
noticias = []

def obtener_pagina(pagina=1):
    # Hacemos una solicitud a la página web https://news.ycombinator.com/?p=1
    response = requests.get(f"{url}?p={pagina}", timeout=10)


    # Creamos un objeto BeautifulSoup con el contenido de la página
    soup = BeautifulSoup(response.content, 'html.parser')

    # Buscamos todas las noticias. 
    # Para eso buscamos los elementos de tipo <td> en el HTML
    # Los links se encuentran en una tabla
    links = soup.find_all('td', class_='title')

    # Iteramos sobre los enlaces encontrados e imprimimos el texto del enlace y su URL
    news = []
    for link in links:
        span_child = list(link.children)[0]
        # Solo usamos el <td> que nos interesa
        if 'titleline' in span_child.attrs['class']:
            a_link = list(span_child.children)[0]
            # Guardamos los links como una lista de diccionarios
            news.append(dict(title=a_link.text, url=a_link.attrs['href']))

    # extraer datos extras como el puntaje, el autor y el tiempo
    datos = []
    lineas = soup.find_all('td', class_='subtext')
    for linea in lineas:
        puntaje = linea.find('span', class_='score')
        autor = linea.find('a', class_='hnuser')
        age = linea.find('span', class_='age')
        #<a href="item?id=47404796">26 comments</a>
        comments = linea.find_all('a')[-1]

        datos.append(dict(puntaje=puntaje.text if puntaje else None, autor=autor.text if autor else None, age=age.text if age else None, comments=comments.text if comments else None))
    
    # Unificar las noticias con los datos extras
    for i in range(len(news)):
        news[i].update(datos[i])

    return news

noticias = obtener_pagina(1)
noticias += obtener_pagina(2)
noticias += obtener_pagina(3)
noticias += obtener_pagina(4)

for i, noticia in enumerate(noticias):
    print(i, noticia)
    if i==99:
        break