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
    siteNoticia = StringVar()

    lbl_aviso = Label(app, text="Selecione uma opção", background="#dde")
    lbl_aviso.place(x=15, y=70)

    rb_g1 = Radiobutton(app, text="Noticias G1", value="g", variable=siteNoticia, background="#dde")
    rb_g1.place(x=15, y=100)
    rb_UOL = Radiobutton(app, text="Noticias UOL", value="o", variable=siteNoticia, background="#dde")
    rb_UOL.place(x=15, y=130)
    rb_Folha = Radiobutton(app, text="Noticias Folha de São Paulo", value="f", variable=siteNoticia, background="#dde")
    rb_Folha.place(x=15, y=160)

    Button(app, text="Gerar PDF", command=lambda: botaoNoticia(txtQtde.get(), app, siteNoticia.get())).place(x=10, y=270, width=100, height=20)
    app.mainloop()

