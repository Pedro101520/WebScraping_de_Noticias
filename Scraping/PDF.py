from .noticias import *

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

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
    titulo_texto = titulo()
    descricao_texto = descricao()
    datalocal_texto = localHora()
    link_texto = links()

    descricao_texto[4] = None

    for i in range(qtde_noticias):
        # Adiciona o título ao conteúdo com quebra de linha
        titulo_formatado = "<b>{}</b>".format(titulo_texto[i])
        conteudo.append(Paragraph(titulo_formatado, estilo_titulo))

        if descricao_texto[i] is not None or descricao_texto != "":
            conteudo.append(Paragraph(str(descricao_texto[i]), estilo_texto))

        # Verifica se há link disponível para a notícia atual
        conteudo.append(Paragraph('<a href="{}">{}</a>'.format(link_texto[i], link_texto[i]), estilo_link))

        # Verifica se há informações de Data e Local disponíveis para a notícia atual
        conteudo.append(Paragraph(datalocal_texto[i], estilo_DataLocal))

        # Adiciona um espaço entre os itens
        conteudo.append(Paragraph("<br/><br/>", estilo_texto))
    pdf.build(conteudo)