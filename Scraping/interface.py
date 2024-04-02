from .PDF import *

from tkinter import *
from tkinter import messagebox

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

    Button(app, text="Gerar PDF", command=lambda: botaoNoticia(txtQtde.get(), app)).place(x=10, y=270, width=100, height=20)
    app.mainloop()