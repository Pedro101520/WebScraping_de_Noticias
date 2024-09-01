from urllib.request import urlopen
from bs4 import BeautifulSoup

url = urlopen("https://www.cnnbrasil.com.br/ultimas-noticias/")
parsed_html = BeautifulSoup(url, "html.parser")

def tituloCNN():
    textoTitulo = []
    titulos = parsed_html.find_all('h3', class_='news-item-header__title')
    for titulo in titulos:
        textoTitulo.append(titulo.get_text())
    return textoTitulo

def HoraCNN():
    armazenaInfo = []
    infos = parsed_html.find_all('span', class_='home__title__date')
    for info in infos:
        conteudo = info.get_text()
        armazenaInfo.append(conteudo)
    return armazenaInfo

def descricaoCNN(qtde_noticias):
    descricao = []
    links = linksCNN()[:qtde_noticias]
    for link in links:
        url = urlopen(link)
        textoDescricao = BeautifulSoup(url, "html.parser")
        descricoes = textoDescricao.find('p', class_={'single-header__excerpt'})
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