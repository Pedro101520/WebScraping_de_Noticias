from urllib.request import urlopen
from bs4 import BeautifulSoup

url = urlopen("https://www1.folha.uol.com.br/ultimas-noticias/")
parsed_html = BeautifulSoup(url, "html.parser")

def tituloFolha():
    textoTitulo = []
    titulos = parsed_html.find_all('div', attrs={'class': 'c-headline__content'})
    for titulo in titulos:
        conteudo = titulo.find('h2').get_text()
        textoTitulo.append(conteudo)
    return textoTitulo

def descricaoFolha():
    textoDescricao = []
    descricoes = parsed_html.find_all('div', attrs={'class': 'c-headline__content'})
    for descricao in descricoes:
        conteudo = descricao.find('p').get_text()
        textoDescricao.append(conteudo)
    return textoDescricao


def linksFolha():
    armazenaLink = []
    links = parsed_html.find_all('div', attrs={'class': 'c-headline__content'})
    for link in links:
        url = link.find('a')
        armazenaLink.append(url.get('href'))
    return armazenaLink

def HoraFolha():
    armazenaInfo = []
    infos = parsed_html.find_all('div', attrs={'class': 'c-headline__content'})
    for info in infos:
        conteudo = info.find('time').get_text()
        armazenaInfo.append(conteudo)
    return armazenaInfo