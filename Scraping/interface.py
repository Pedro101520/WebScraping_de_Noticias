from .PDF import *
from tkinter import *
from tkinter import messagebox

def botaoNoticia(qtdeNoticia, siteNoticia):
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
    except PermissionError:
        messagebox.showerror("Aviso", "Feche o arquivo PDF e tente novamente!")
    except UnboundLocalError:
        messagebox.showerror("Aviso", "Selecione uma opção!")

def sair(app): app.destroy()

def window():
    app = Tk()
    app.title("Ultimas Noticias")
    app.geometry("500x300")
    app.configure(background='#dde')
    Label(
        app,
        text = "Quantidade de noticias - Entre 1 a 10:",
        background = "#dde",
        foreground = "#000",
        anchor = W
    ).place(x=10, y=10, width=200, height=20)
    txtQtde=Entry(app)
    txtQtde.place(x=225, y=10, width=50, height=20)

    siteNoticia = StringVar(value=0)
    lbl_aviso = Label(app, text="Selecione uma opção", background="#dde")
    lbl_aviso.place(x=15, y=70)
    rb_g1 = Radiobutton(app, text="G1", value="g", variable=siteNoticia, background="#dde")
    rb_g1.place(x=15, y=100)
    rb_UOL = Radiobutton(app, text="UOL", value="o", variable=siteNoticia, background="#dde")
    rb_UOL.place(x=15, y=130)
    rb_Folha = Radiobutton(app, text="Folha de São Paulo", value="f", variable=siteNoticia, background="#dde")
    rb_Folha.place(x=15, y=160)
    rb_CNN = Radiobutton(app, text="CNN", value="c", variable=siteNoticia, background="#dde")
    rb_CNN.place(x=15, y=190)
    rb_jovem = Radiobutton(app, text="Jovem Pan", value="j", variable=siteNoticia, background="#dde")
    rb_jovem.place(x=15, y=220)

    Button(app, text="Gerar PDF", command=lambda: botaoNoticia(txtQtde.get(), siteNoticia.get())).place(x=10, y=270, width=100, height=20)
    Button(app, text="Sair", command=lambda: sair(app)).place(x=120, y=270, width=100, height=20)
    app.mainloop()