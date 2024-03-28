from urllib.request import urlopen
from bs4 import BeautifulSoup
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

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

def localHora():
    armazenaInfo = []
    infos = parsed_html.find_all('div', attrs={'class': 'feed-post-metadata'})
    for info in infos[:5]:
        span =  info.find_all('span')
        infoHora = span[0].get_text()
        infoLocal = span[1].get_text()
        armazenaInfo.append(infoHora + ' - ' + infoLocal)
    return armazenaInfo

def geraPdf():
    pdf = SimpleDocTemplate("Ultimas_Noticias.pdf", pagesize=letter)

    # Estilo para o titulo
    estilo_titulo = ParagraphStyle(
        "titulo",
        parent=getSampleStyleSheet()["Title"],
        fontSize=12,
        textColor=colors.black
    )

    # Estilo para o texto
    estilo_texto = ParagraphStyle(
        "texto",
        parent=getSampleStyleSheet()["Normal"],
        fontSize=10,
        textColor=colors.black
    )

    # Estilo para o link
    estilo_link = ParagraphStyle(
    "link",
    parent=getSampleStyleSheet()["Normal"],
    fontSize=10,
    textColor=colors.blue
    )

    # Estilo para Data e Local
    estilo_DataLocal = ParagraphStyle(
    "DataLocal",
    parent=getSampleStyleSheet()["Normal"],
    fontSize=8,
    textColor=colors.gray
    )

    # Array para armazenar os elementos do PDF
    conteudo = []

    # Adiciona os títulos, descrições e links ao conteúdo do PDF
    for i in range(5):
        titulo_texto = titulo()[i]
        descricao_texto = descricao()[i]
        datalocal_texto = localHora()[i]
        link_texto = links()[i]
        
        # Adiciona o título ao conteúdo com quebra de linha
        titulo_formatado = "<b>{}</b>".format(titulo_texto)
        conteudo.append(Paragraph(titulo_formatado, estilo_titulo))

        # Adiciona a descrição
        conteudo.append(Paragraph(descricao_texto, estilo_texto))

        # Adiciona os Links
        conteudo.append(Paragraph('<a href="{}">{}</a>'.format(link_texto, link_texto), estilo_link))
        
        # Adiciona informações de Data e local
        conteudo.append(Paragraph(datalocal_texto, estilo_DataLocal))
        
        # Adiciona um espaço entre os itens
        conteudo.append(Paragraph("<br/><br/>", estilo_texto))
    pdf.build(conteudo)

geraPdf()

# for i in range(0, 5):
#     print(localHora()[i])