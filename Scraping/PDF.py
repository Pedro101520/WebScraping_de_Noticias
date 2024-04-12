from .newsG1 import *
from .newsUOL import *
from .newsFolha import *
from .newsCNN import *
from .newsJovem import *

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

def geraPdf(qtde_noticias, siteNoticia):
    estilo_titulo = ParagraphStyle(
        "titulo",
        parent=getSampleStyleSheet()["Title"],
        fontSize=12,
        textColor=colors.black
    )
    estilo_texto = ParagraphStyle(
        "texto",
        parent=getSampleStyleSheet()["Normal"],
        fontSize=10,
        textColor=colors.black
    )
    estilo_link = ParagraphStyle(
        "link",
        parent=getSampleStyleSheet()["Normal"],
        fontSize=10,
        textColor=colors.blue
    )
    estilo_DataLocal = ParagraphStyle(
        "DataLocal",
        parent=getSampleStyleSheet()["Normal"],
        fontSize=8,
        textColor=colors.gray
    )

    conteudo = []

    if(siteNoticia == 'o'):
        titulo_texto = tituloUol()
        datalocal_texto = HoraUol()
        link_texto = linksUol()
        pdf = SimpleDocTemplate("Noticias_UOL.pdf", pagesize=letter)
    elif(siteNoticia == 'g'):
        titulo_texto = tituloG1()
        datalocal_texto = localHoraG1()
        link_texto = linksG1()
        descricao_texto = descricaoG1()
        pdf = SimpleDocTemplate("Noticias_G1.pdf", pagesize=letter)
    elif(siteNoticia == 'f'):
        titulo_texto = tituloFolha()
        datalocal_texto = HoraFolha()
        link_texto = linksFolha()
        descricao_texto = descricaoFolha()
        pdf = SimpleDocTemplate("Noticias_FolhaDeSaoPaulo.pdf", pagesize=letter)
    elif(siteNoticia == 'c'):
        titulo_texto = tituloCNN()
        datalocal_texto = HoraCNN()
        link_texto = linksCNN()
        descricao_texto = descricaoCNN(qtde_noticias)
        pdf = SimpleDocTemplate("Noticias_CNN.pdf", pagesize=letter)
    elif(siteNoticia == 'j'):
        titulo_texto = tituloJovem()
        datalocal_texto = HoraJovem()
        link_texto = linksJovem()
        descricao_texto = descricaoJovem(qtde_noticias)
        pdf = SimpleDocTemplate("Noticias_JovemPan.pdf", pagesize=letter)

    for i in range(qtde_noticias):
        titulo_formatado = "<b>{}</b>".format(titulo_texto[i])
        conteudo.append(Paragraph(titulo_formatado, estilo_titulo))

        if siteNoticia == 'g' or siteNoticia == 'f' or siteNoticia == 'c' or siteNoticia == 'j':
            if descricao_texto[i] != "":
                conteudo.append(Paragraph(descricao_texto[i], estilo_texto))
            else:
                conteudo.append(Paragraph("Descrição indisponível", estilo_texto))

        conteudo.append(Paragraph('<a href="{}">{}</a>'.format(link_texto[i], link_texto[i]), estilo_link))
        conteudo.append(Paragraph(datalocal_texto[i], estilo_DataLocal))
        conteudo.append(Paragraph("<br/><br/>", estilo_texto))
    pdf.build(conteudo)