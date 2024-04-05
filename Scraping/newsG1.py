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

def descricaoG1(qtde_noticias):
    textoDescricao = []
    descricoes = parsed_html.find_all('div', attrs={'class': 'feed-post-body-resumo'})
    for i in range(qtde_noticias):
        if i < len(descricoes):
            descricao = descricoes[i]
            conteudo = descricao.find('p').get_text()
            textoDescricao.append(conteudo)
            if descricao == 'None':
                print("oi")    
        else:
            textoDescricao.append("Descrição não disponível")
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