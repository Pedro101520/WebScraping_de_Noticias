from urllib.request import urlopen
from bs4 import BeautifulSoup

url = urlopen("https://jovempan.com.br/ultimas")
parsed_html = BeautifulSoup(url, "html.parser")

def tituloJovem():
    textoTitulo = []
    titulos = parsed_html.find_all('h2', attrs={'class': 'post-title'})
    for titulo in titulos:
        conteudo = titulo.find('a').get_text()
        textoTitulo.append(conteudo)
    return textoTitulo

def descricaoJovem(qtde_noticias):
    descricao = []
    links = linksJovem()[:qtde_noticias]
    for link in links:
        url = urlopen(link)
        textoDescricao = BeautifulSoup(url, "html.parser")
        descricoes = textoDescricao.find('h3', attrs={'post-description'})
        if not descricoes:
            descricao.append("")
        else:
            descricao.append(descricoes.get_text())
    return descricao


def linksJovem():
    armazenaLink = []
    links = parsed_html.find_all('h2', attrs={'class': 'post-title'})
    for link in links:
        url = link.find('a')
        armazenaLink.append(url.get('href'))
    print(armazenaLink)
    return armazenaLink

def HoraJovem():
    armazenaInfo = []
    infos = parsed_html.find_all('span', attrs={'class': 'date'})
    for info in infos:
        conteudo = info.get_text()
        armazenaInfo.append(conteudo)
    return armazenaInfo