from urllib.request import urlopen
from bs4 import BeautifulSoup

url = urlopen("https://www.cnnbrasil.com.br/ultimas-noticias/")
parsed_html = BeautifulSoup(url, "html.parser")

def tituloCNN():
    textoTitulo = []
    titulos = parsed_html.find_all('div', attrs={'class': 'home__list__tag'})
    for titulo in titulos:
        conteudo = titulo.find('h3').get_text()
        textoTitulo.append(conteudo)
    return textoTitulo

def HoraCNN():
    armazenaInfo = []
    infos = parsed_html.find_all('div', attrs={'class': 'latest__news__infos'})
    for info in infos:
        conteudo = info.find('span').get_text()
        armazenaInfo.append(conteudo)
    return armazenaInfo

def descricaoCNN():
    descricao = []
    links = linksCNN()[:10]
    for link in links:
        url = urlopen(link)
        textoDescricao = BeautifulSoup(url, "html.parser")
        descricoes = textoDescricao.find('p', attrs={'post__excerpt'})
        if not descricoes:
            descricao.append("")
        else:
            descricao.append(descricoes.get_text())
    return descricao

def linksCNN():
    armazenaLink = []
    links = parsed_html.find_all('li', attrs={'class': 'home__list__item'})
    for link in links:
        url = link.find('a')
        armazenaLink.append(url.get('href'))
    return armazenaLink