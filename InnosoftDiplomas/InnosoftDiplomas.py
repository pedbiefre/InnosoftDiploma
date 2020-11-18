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
    raiz.geometry('800x200')

    img = ImageTk.PhotoImage(Image.open('/home/blackylyzard/Escritorio/EJmC4M8W4AEf0d7.jpg'))
    canvas = Canvas(raiz, width=800, height=200)
    canvas.pack()
    canvas.create_image(0,0,anchor=NW, image=img)
    panel = Label(raiz, image=img)
    raiz.mainloop()

if __name__ == "__main__":
    ventana_principal()