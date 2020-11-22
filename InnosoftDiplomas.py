import sys
import os
import time
from tkinter import *

from PIL import ImageTk, Image

from innosoft_diplomas.diploma_automatico import diplomasGenerador
from innosoft_diplomas.diploma_excepcional import diplomasExc

def ventana_principal():  
    raiz = Tk()

    menu = Menu(raiz)

    #DIPLOMAS AUTOMATICOS
    menudatos = Menu(menu, tearoff=0)
    menudatos.add_command(label="Generar", command=diplomasGenerador)
    menu.add_cascade(label="Generación Automática", menu=menudatos)

    #DIPLOMAS EXTRAS
    menudatos = Menu(menu, tearoff=0)
    menudatos.add_command(label="Diplomas Extraordinarios", command= lambda: diplomasExc("extraordinario"))
    menudatos.add_command(label="Diplomas Ponentes", command= lambda: diplomasExc("ponente"))
    menudatos.add_command(label="Diplomas Organizadores", command= lambda: diplomasExc("organizador"))
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