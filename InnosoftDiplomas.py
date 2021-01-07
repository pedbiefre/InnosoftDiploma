#!/usr/bin/python
import sys
import os
import time
from tkinter import *

from PIL import ImageTk, Image
import PIL

from innosoft_diplomas.diploma_automatico import  diplomasGeneradorOrganizador, formularioAutomaticoAsistencia
from innosoft_diplomas.diploma_excepcional import diplomasExc
from innosoft_diplomas.edicion import selecFuente
from innosoft_diplomas.parametros import *
from innosoft_diplomas.emails import *

parametros = Parametros('Philosopher')

#Función que llama a la creación de la aplicación mediante Tkinter
def ventana_principal():  
    raiz = Tk()
    #Inicialización del Menú
    menu = Menu(raiz)

    #DIPLOMAS AUTOMATICOS
    menudatos = Menu(menu, tearoff=0)
    menudatos.add_command(label="Generar Diplomas de Asistencia", command=formularioAutomaticoAsistencia)
    menudatos.add_command(label="Generar Diplomas de Organizadores", command=diplomasGeneradorOrganizador)
    menu.add_cascade(label="Generación Automática", menu=menudatos)

    #DIPLOMAS EXTRAS
    menudatos = Menu(menu, tearoff=0)
    menudatos.add_command(label="Diplomas Extraordinarios", command= lambda: diplomasExc("extraordinario", parametros))
    menudatos.add_command(label="Diplomas Ponentes", command= lambda: diplomasExc("ponente", parametros))
    menudatos.add_command(label="Diplomas Organizadores", command= lambda: diplomasExc("organizador", parametros))
    menu.add_cascade(label="Diplomas Especiales", menu=menudatos)

    #OPCIONES DE DIPLOMA
    menudatos = Menu(menu, tearoff=0)
    menu.add_cascade(label="Opciones", menu=menudatos)
    menudatos.add_command(label="Seleccionar fuentes", command=lambda: selecFuente(parametros))

    #ENVIAR CORREOS
    menudatos = Menu(menu, tearoff=0)
    menu.add_cascade(label="Envío automático", menu=menudatos)
    menudatos.add_command(label="Enviar Diplomas por Correo", command=lambda: login())

    #SALIR
    menu.add_cascade(label="Salir", command = raiz.quit)

    #Elementos de personalización para las ventanas
    raiz.title("Innosoft Diplomas")
    raiz.config(menu=menu)
    raiz.geometry('870x340')

    #Imagen de fondo de la aplicación
    fp = open("./resources/images/innosoftDiploamas.png","rb")
    image = PIL.Image.open(fp)
    photo = PIL.ImageTk.PhotoImage(image)
    canvas = Canvas(raiz, width=870, height=340)
    canvas.pack()
    canvas.create_image(0,0,anchor=NW, image=photo)

    raiz.mainloop()


if __name__ == "__main__":
    ventana_principal()