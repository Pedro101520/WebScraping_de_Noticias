#Lembrar que no site do G1 tem como pegar o link das noticias
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = urlopen("https://g1.globo.com/ultimas-noticias/")
parsed_html = BeautifulSoup(url, "html.parser")

def titulo():
    textoTitulo = []
    titulos = parsed_html.find_all('div', attrs={'class': 'feed-post-body-title'})
    for titulo in titulos[:5]:
        conteudo = titulo.find('p').get_text()
        textoTitulo.append(conteudo)
    return textoTitulo

def descricao():
    textoDescricao = []
    descricoes = parsed_html.find_all('div', attrs={'class': 'feed-post-body-resumo'})
    for descricao in descricoes[:5]:
        conteudo = descricao.find('p').get_text()
        textoDescricao.append(conteudo)
    return textoDescricao

def links():
    armazenaLink = []
    links = parsed_html.find_all('div', attrs={'class': 'feed-post-body-title'})
    for link in links[:5]:
        url = link.find('a')
        armazenaLink.append(url.get('href'))
    return armazenaLink

def formataConteudo():
    for i in range(0, 5):
        print(titulo()[i])
        print(descricao()[i])
        print(links()[i])
        print('\n')

formataConteudo()