import sys
import os
import time
from tkinter import *

from PIL import ImageTk, Image

from app.diploma_automatico import diplomasGenerador
from app.diploma_extraordinario import diplomasExt
from app.diploma_ponente import diplomasPon

def ventana_principal():  
    raiz = Tk()

    menu = Menu(raiz)

    #DIPLOMAS AUTOMATICOS
    menudatos = Menu(menu, tearoff=0)
    menudatos.add_command(label="Generar", command=diplomasGenerador)
    menu.add_cascade(label="Generación Automática", menu=menudatos)

    #DIPLOMAS EXTRAS
    menudatos = Menu(menu, tearoff=0)
    menudatos.add_command(label="Diplomas Extraordinarios", command= diplomasExt)
    menudatos.add_command(label="Diplomas Ponente", command= diplomasPon)
    menu.add_cascade(label="Diplomas Especiales", menu=menudatos)

    #SALIR
    menu.add_cascade(label="Salir", command = raiz.quit)

    raiz.title("Innosoft Diplomas")
    raiz.config(menu=menu)
    raiz.geometry('870x340')
    raiz.iconbitmap("./resources/images/innosoft.ico")

    img = ImageTk.PhotoImage(Image.open('./resources/images/innosoftDiploamas.png'))
    canvas = Canvas(raiz, width=870, height=340)
    canvas.pack()
    canvas.create_image(0,0,anchor=NW, image=img)

    raiz.mainloop()

if __name__ == "__main__":
    ventana_principal()