from .PDF import *

from tkinter import *
from tkinter import messagebox

def botaoNoticia(qtdeNoticia, app, siteNoticia):
    try:
        if not(qtdeNoticia.isdigit()):
            messagebox.showerror("Atenção", "Digite apenas numeros")
        else:
            qtdeNoticia = int(qtdeNoticia)
            if qtdeNoticia < 1 or qtdeNoticia > 10:
                messagebox.showerror("Atenção", "Apenas numeros entre 1 a 10")
            else:
                geraPdf(qtdeNoticia, siteNoticia)
                messagebox.showinfo("Aviso", "PDF Gerado!")
                app.destroy()
    except PermissionError:
        messagebox.showerror("Aviso", "Feche o arquivo PDF e tente novamente!")

def window():
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

    txtQtde=Entry(app)
    txtQtde.place(x=225, y=10, width=50, height=20)

    # Parte resposanvel pelos Radios Buttons
    siteNoticia = []

    lbl_aviso = Label(app, text="Selecione uma ou mais opções", background="#dde")
    lbl_aviso.place(x=15, y=70)

    cb_g1 = Checkbutton(app, text="Noticias G1", onvalue=siteNoticia.insert(0, 'g'), offvalue="", variable=siteNoticia, background="#dde")
    cb_g1.place(x=15, y=100)
    cb_UOL = Checkbutton(app, text="Noticias UOL", onvalue=siteNoticia.insert(1, 'o'), offvalue="", variable=siteNoticia, background="#dde")
    cb_UOL.place(x=15, y=130)
    cb_Folha = Checkbutton(app, text="Noticias Folha de São Paulo", onvalue=siteNoticia.insert(2, 'f'), offvalue="", variable=siteNoticia, background="#dde")
    cb_Folha.place(x=15, y=160)
    cb_CNN = Checkbutton(app, text="Noticias CNN", onvalue=siteNoticia.insert(3, 'c'), offvalue="", variable=siteNoticia, background="#dde")
    cb_CNN.place(x=15, y=190)
    cb_jovem = Checkbutton(app, text="Noticias Jovem Pan", onvalue=siteNoticia.insert(4, 'j'), offvalue="", variable=siteNoticia, background="#dde")
    cb_jovem.place(x=15, y=220)

    Button(app, text="Gerar PDF", command=lambda: botaoNoticia(txtQtde.get(), app, siteNoticia)).place(x=10, y=270, width=100, height=20)
    app.mainloop()

