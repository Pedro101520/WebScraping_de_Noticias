import requests
from bs4 import BeautifulSoup

url = "https://noticias.uol.com.br/ultimas/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive"
}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    parsed_html = BeautifulSoup(response.text, "html.parser")

    def tituloUol():
        textoTitulo = []
        titulos = parsed_html.find_all('div', attrs={'class': 'thumb-caption'})
        for titulo in titulos:
            conteudo = titulo.find('h3').get_text()
            textoTitulo.append(conteudo)
        return textoTitulo

    def HoraUol():
        armazenaInfo = []
        infos = parsed_html.find_all('div', attrs={'class': 'thumb-caption'})
        for info in infos:
            conteudo = info.find('time').get_text()
            armazenaInfo.append(conteudo)
        return armazenaInfo

    def linksUol():
        armazenaLink = []
        links = parsed_html.find_all('div', attrs={'class': 'thumbnails-wrapper'})
        for link in links:
            url = link.find('a')
            armazenaLink.append(url.get('href'))
        return armazenaLink

    titulos = tituloUol()
    horas = HoraUol()
    links = linksUol()


except requests.exceptions.HTTPError as e:
    print(f"Erro ao acessar a página: {e}")
except Exception as e:
    print(f"Erro: {e}")
