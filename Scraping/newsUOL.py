from urllib.request import urlopen
from bs4 import BeautifulSoup

url = urlopen("https://noticias.uol.com.br/ultimas/")
parsed_html = BeautifulSoup(url, "html.parser")

def titulo():
    textoTitulo = []
    titulos = parsed_html.find_all('div', attrs={'class': 'thumb-caption'})
    for titulo in titulos:
        conteudo = titulo.find('h3').get_text()
        textoTitulo.append(conteudo)
    return textoTitulo

# localHora
def Hora():
    armazenaInfo = []
    infos = parsed_html.find_all('div', attrs={'class': 'thumb-caption'})
    for info in infos:
        conteudo = info.find('time').get_text()
        armazenaInfo.append(conteudo)
    return armazenaInfo

def links():
    armazenaLink = []
    links = parsed_html.find_all('div', attrs={'class': 'thumbnails-wrapper'})
    for link in links:
        url = link.find('a')
        armazenaLink.append(url.get('href'))
    return armazenaLink

print(Hora())