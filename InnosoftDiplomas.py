#!/usr/bin/python
import sys
import os
import time
from tkinter import *

from PIL import ImageTk, Image

from innosoft_diplomas.diploma_automatico import diplomasGenerador
from innosoft_diplomas.diploma_excepcional import diplomasExc
from innosoft_diplomas.edicion import selecFuente
from innosoft_diplomas.parametros import *

parametros = Parametros('Philosopher')

def ventana_principal():  
    raiz = Tk()

    menu = Menu(raiz)



    #DIPLOMAS AUTOMATICOS
    menudatos = Menu(menu, tearoff=0)
    menudatos.add_command(label="Generar", command=diplomasGenerador)
    menu.add_cascade(label="Generación Automática", menu=menudatos)

    #DIPLOMAS EXTRAS
    menudatos = Menu(menu, tearoff=0)
    menudatos.add_command(label="Diplomas Extraordinarios", command= lambda: diplomasExc("extraordinario", parametros))
    menudatos.add_command(label="Diplomas Ponentes", command= lambda: diplomasExc("ponente"))
    menudatos.add_command(label="Diplomas Organizadores", command= lambda: diplomasExc("organizador"))
    menu.add_cascade(label="Diplomas Especiales", menu=menudatos)

    #OPCIONES DE DIPLOMA
    menudatos = Menu(menu, tearoff=0)
    menu.add_cascade(label="Opciones", menu=menudatos)
    menudatos.add_command(label="Seleccionar fuentes", command=lambda: selecFuente(parametros))

    #SALIR
    menu.add_cascade(label="Salir", command = raiz.quit)

    raiz.title("Innosoft Diplomas")
    raiz.config(menu=menu)
    raiz.geometry('870x340')

    img = ImageTk.PhotoImage(Image.open('./resources/images/innosoftDiploamas.png'))
    canvas = Canvas(raiz, width=870, height=340)
    canvas.pack()
    canvas.create_image(0,0,anchor=NW, image=img)

    raiz.mainloop()


if __name__ == "__main__":
    ventana_principal()