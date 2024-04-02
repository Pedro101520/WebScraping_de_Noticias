from urllib.request import urlopen
from bs4 import BeautifulSoup
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from tkinter import *
from tkinter import messagebox

url = urlopen("https://g1.globo.com/ultimas-noticias/")
parsed_html = BeautifulSoup(url, "html.parser")

def titulo():
    textoTitulo = []
    titulos = parsed_html.find_all('div', attrs={'class': 'feed-post-body-title'})
    for titulo in titulos:
        if titulo is not None:
            conteudo = titulo.find('p').get_text()
        else:
            conteudo = ' '
        textoTitulo.append(conteudo)
    return textoTitulo

def descricao():
    textoDescricao = []
    descricoes = parsed_html.find_all('div', attrs={'class': 'feed-post-body-resumo'})
    for descricao in descricoes:
        if not descricao:
            textoDescricao.append('')
        else:
            conteudo = descricao.find('p')
            textoDescricao.append(conteudo.get_text())
    return textoDescricao

def links():
    armazenaLink = []
    links = parsed_html.find_all('div', attrs={'class': 'feed-post-body-title'})
    for link in links:
        url = link.find('a')
        armazenaLink.append(url.get('href'))
    return armazenaLink

def localHora():
    armazenaInfo = []
    infos = parsed_html.find_all('div', attrs={'class': 'feed-post-metadata'})
    for info in infos:
        span =  info.find_all('span')
        if span is not None:
            infoHora = span[0].get_text()
            infoLocal = span[1].get_text()
        else:
            infoHora = ' '
            infoLocal = ' '
        armazenaInfo.append(infoHora + ' - ' + infoLocal)
    return armazenaInfo

def geraPdf(qtde_noticias):
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
    for i in range(qtde_noticias):
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

def botaoNoticia(qtdeNoticia, app):
    try:
        if not(qtdeNoticia.isdigit()):
            messagebox.showerror("Atenção", "Digite apenas numeros")
        else:
            qtdeNoticia = int(qtdeNoticia)
            if qtdeNoticia < 1 or qtdeNoticia > 10:
                messagebox.showerror("Atenção", "Apenas numeros entre 1 a 10")
            else:
                geraPdf(qtdeNoticia)
                messagebox.showinfo("Aviso", "PDF Gerado!")
                app.destroy()
    except PermissionError:
        messagebox.showerror("Aviso", "Feche o arquivo PDF e tente novamente!")

def interface():
    app = Tk()
    app.title("Ultimas Noticias")
    app.geometry("500x300")
    app.configure(background='#dde')

    Label(
        app,
        text = "Quantidade de noticias - Entre 1 a 10:",
        background = "#dde",
        foreground = "#009",
        anchor = W
    ).place(x=10, y=10, width=200, height=20)

    # txtQtde = Spinbox(app, from_=1, to=10)
    txtQtde=Entry(app)
    txtQtde.place(x=225, y=10, width=50, height=20)

    Button(app, text="Gerar PDF", command=lambda: botaoNoticia(txtQtde.get(), app)).place(x=10, y=270, width=100, height=20)
    app.mainloop()

interface()