from urllib.request import urlopen
from bs4 import BeautifulSoup

url = urlopen("https://g1.globo.com/ultimas-noticias/")
parsed_html = BeautifulSoup(url, "html.parser")

def tituloG1():
    textoTitulo = []
    titulos = parsed_html.find_all('div', attrs={'class': 'feed-post-body-title'})
    for titulo in titulos:
        conteudo = titulo.find('p').get_text()
        textoTitulo.append(conteudo)
    return textoTitulo

def descricaoG1():
    textoDescricao = []
    body = parsed_html.find_all('div', attrs={'class': 'feed-post-body'})
    j = 0
    for i in body:
        descricoes = i.find('div', attrs={'class': 'feed-post-body-resumo'})
        if not descricoes:
            print("Não há descrição para esta notícia no momento.", j)
            textoDescricao.append("")
        else:
            print("Descrição disponivel", j)
            texto = descricoes.find('p')
            textoDescricao.append(texto.get_text())
        j += 1
    return textoDescricao












def linksG1():
    armazenaLink = []
    links = parsed_html.find_all('div', attrs={'class': 'feed-post-body-title'})
    for link in links:
        url = link.find('a')
        armazenaLink.append(url.get('href'))
    return armazenaLink

def localHoraG1():
    armazenaInfo = []
    infos = parsed_html.find_all('div', attrs={'class': 'feed-post-metadata'})
    for info in infos:
        span =  info.find_all('span')
        infoHora = span[0].get_text()
        infoLocal = span[1].get_text()
        armazenaInfo.append(infoHora + ' - ' + infoLocal)
    return armazenaInfo