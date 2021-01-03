import pandas as pd
import sys
import os
import time
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import math
import pathlib
import tkinter as tk

from reportlab.lib.pagesizes import landscape, A4, inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont


def formularioAutomaticoAsistencia():

    def generar():
        #1 y 2 son los int de control del método diplomasGeneradorAsistencia: si 1 se crea un diploma basico, si 2 se crea un diploma custom 
        if(opcion.get()==1):
            diplomasGeneradorAsistencia(opcion.get())
        if(opcion.get()==2):
            textos = [title.get(),subtitle.get(),info.get(),info2.get(),info3.get(),info4.get(),fecha.get(),plantilla.get()]
            diplomasGeneradorAsistencia(opcion.get(),textos)
    

    root = Toplevel()
    root.title("Innosoft Diplomas")
    root.geometry('820x300')

    title = StringVar(root, value= "INNOSOFT DAYS")
    subtitle = StringVar(root, value= "confiere el siguiente certificado a:")
    info = StringVar(root, value="por su asistencia a ")
    info2 = StringVar(root, value=" evento/s durante las jornadas de Innosoft Days")
    info3 = StringVar(root,value="con una dedicación total de ")
    info4 = StringVar(root, value=" hora/s")
    fecha = StringVar(root, value=time.strftime("%d/%m/%y"))
    plantilla= StringVar(root, value="./resources/images/PLANTILLA.jpg")

    title_label = Label(root,text="Título:").grid(row=3,column=0,sticky='e')
    title_entry = Entry(root,textvariable=title)
    title_entry.grid(row=3,column=1,padx=2, pady=2, sticky='we', columnspan=9)

    subtitle_label = Label(root,text="Subtítulo:").grid(row=4,column=0,sticky='e')
    subtitle_entry = Entry(root,textvariable=subtitle)
    subtitle_entry.grid(row=4,column=1,padx=2, pady=2, sticky='we', columnspan=9)

    info_label = Label(root,text="Información:").grid(row=5,column=0,sticky='e')
    info_entry = Entry(root,textvariable=info)
    info_entry.grid(row=5,column=1,padx=2, pady=2, sticky='we', columnspan=1)
    info_num_eventos = Label(root,text="X").grid(row=5,column=2,sticky='e')
    info_entry2 = Entry(root,textvariable=info2)
    info_entry2.grid(row=5,column=3,padx=2, pady=2, sticky='we', columnspan=5)
    info_entry3 = Entry(root,textvariable=info3)
    info_entry3.grid(row=6,column=1,padx=2, pady=2, sticky='we', columnspan=5)
    info_num_horas = Label(root,text="Y").grid(row=6,column=2,sticky='e')
    info_entry4 = Entry(root,textvariable=info4)
    info_entry4.grid(row=6,column=3,padx=2, pady=2, sticky='we', columnspan=1)
    
    

    fecha = StringVar(root, value=time.strftime("%d/%m/%y"))
    date_label = Label(root,text="Fecha:").grid(row=7,column=0,sticky='e')
    date_entry = Entry(root,textvariable=fecha)
    date_entry.grid(row=7,column=1,padx=2, pady=2, sticky='we', columnspan=1)

    def get_plantilla():
        filename = filedialog.askopenfilename(initialdir = pathlib.Path().absolute(),title = "Seleccione la plantilla del diploma",filetypes = [('Image files', '.png'),
               ('Image files', '.jpg')])
        src_entry.delete(0,END)
        src_entry.insert(0,filename)

    src_label = Label(root,text="Plantilla:").grid(row=7,column=0,sticky='e')
    src_entry = Entry(root,textvariable=plantilla)
    src_entry.grid(row=8,column=1,padx=2, pady=2, sticky='we', columnspan=9)
    src_buttom= Button(root, text="Examinar", command=get_plantilla)
    src_buttom.grid(row=8,column=12,padx=2, pady=2, sticky='we')

    entries = []
    entries.append(title_entry)
    entries.append(subtitle_entry)
    entries.append(info_entry)
    entries.append(info_entry2)
    entries.append(info_entry3)
    entries.append(info_entry4)
    entries.append(date_entry)
    entries.append(src_entry)

    #añadir los parametros de entrada para que no permitan la edición cuando esté en diseño basico
    def disable_entries():
        for e in entries:
            e.configure(state="disabled")
            e.update()

    def enable_entries():
         for e in entries:
            e.configure(state="normal")
            e.update()
            
    opcion = IntVar()

    radio1 = Radiobutton(root, text="BÁSICO", variable=opcion, value=1, command=disable_entries)
    radio2 = Radiobutton(root, text="CUSTOM", variable=opcion, value=2, command=enable_entries)

    enun = Label(root,text="Seleccione BÁSICO para usar la plantilla determinada \n y la fuente escogida en opciones.\n Seleccione CUSTOM para configurar los campos del diploma.")
    enun.grid(row=0,column=3)
    radio1.grid(row=1,column=0)
    radio2.grid(row=1,column=1)
    
    enun2 = Label(root,text="Configuración Diploma Customizado de Asistencia")
    enun2.grid(row=2,column=3)

    generar_buttom=Button(root, text="Generar", command=generar)
    generar_buttom.grid(row=9,column=5)
    

def pdfAutomaticoAsistenciaCustom(nombre, apellidos, eventos_asistidos, horas_totales,textos):
    title= str(textos[0])
    subtitle=str(textos[1])
    info=str(textos[2])
    info2=str(textos[3])
    info3=str(textos[4])
    info4=str(textos[5])
    fecha=str(textos[6])
    plantilla=str(textos[7])
    pdfmetrics.registerFont(TTFont('Philosopher', './resources/fonts/Philosopher-Italic.ttf'))
    c = canvas.Canvas("./Diplomas/DiplomasAsistencia/Diploma-Asistente-CUSTOM-"+apellidos+"-"+nombre+".pdf", pagesize=landscape(A4))
    c.drawImage(plantilla, 0, 0, width = 11.6 * inch, height = 8.4 * inch)
    c.setFont('Philosopher', 27)
    c.setTitle('Diploma - ' + nombre + apellidos)
    c.drawCentredString(5.75 * inch, 5.8 * inch, (title))
    c.drawCentredString(5.75 * inch, 5.2 * inch, (subtitle))
    c.drawCentredString(5.75 * inch, 4.7 * inch, (nombre))
    c.drawCentredString(5.75 * inch, 4.1 * inch, (apellidos))
    c.drawString(0.75 * inch, 3.55 * inch, (info))
    c.drawCentredString(4.2 * inch, 3.55 * inch, (str(eventos_asistidos)))
    c.drawString(4.5 * inch, 3.55 * inch, (info2))
    c.drawString(1.75 * inch, 2.9 * inch, (info3))
    c.drawCentredString(6.8 * inch, 2.9 * inch, (str(horas_totales)))
    c.drawString(7.5 * inch, 2.9 * inch, (info4))
    c.drawCentredString(5.75 * inch, 1.9 * inch, fecha)
    c.save()

def pdfAutomaticoAsistenciaBasico(nombre, apellidos,eventos_asistidos,horas_totales):
    pdfmetrics.registerFont(TTFont('Philosopher', './resources/fonts/Philosopher-Italic.ttf'))
    c = canvas.Canvas("./Diplomas/DiplomasAsistencia/Diploma-Asistente-"+apellidos+"-"+nombre+".pdf", pagesize=landscape(A4))
    c.drawImage("./resources/images/Diploma Asistencia.jpg", 0, 0, width = 11.6 * inch, height = 8.4 * inch)
    c.setFont('Philosopher', 27)
    c.setTitle('Diploma - ' + nombre + apellidos)
    c.drawCentredString(5.75 * inch, 4.7 * inch, (nombre))
    c.drawCentredString(5.75 * inch, 4.1 * inch, (apellidos))
    c.drawCentredString(4.2 * inch, 3.55 * inch, (str(eventos_asistidos)))
    c.drawCentredString(6.8 * inch, 2.9 * inch, (str(horas_totales)))
    c.drawCentredString(5.75 * inch, 1.9 * inch, (time.strftime("%d/%m/%y")))
    c.save()

def diplomasGeneradorAsistencia(control,textos):
    filename = filedialog.askopenfilename(initialdir = pathlib.Path().absolute(),title = "Seleccione el fichero con los datos de asistencia",filetypes = [("Excel files", "*.xlsx")])
    df = pd.read_excel(filename,  header=None)
    contador = asistenciaAuxiliar(df,control,textos)
    messagebox.showinfo("Diplomas creados","Se han creado un total de " + str(contador) + " diplomas de asistencia. Se han almacenado en /Diplomas/DiplomasAsistencia")
    

def asistenciaAuxiliar(dataFrame,control,textos):
    numero_filas = dataFrame.shape[0]
    contador = 0
    for i in range (1,numero_filas):
        
        columna = dataFrame.iloc[i].values
        apellidos = columna[1]   
        nombre = columna[2]
        eventos_asistidos = columna[10]
        try:
            horas_totales = float(columna[17])
        except:
            continue
        if not(isinstance(horas_totales, float)) or horas_totales <= 0 or  not(isinstance(nombre, str)) or not(isinstance(apellidos, str)) or not(isinstance(eventos_asistidos, int)):
            continue
        if(control==1):
            pdfAutomaticoAsistenciaBasico(nombre, apellidos, eventos_asistidos, horas_totales)
        if(control==2):
            pdfAutomaticoAsistenciaCustom(nombre, apellidos, eventos_asistidos, horas_totales, textos)
        contador = contador + 1
    return contador

def pdfAutomaticoOrganizador(nombre, apellidos,comite):
        
    pdfmetrics.registerFont(TTFont('Philosopher', './resources/fonts/Philosopher-Italic.ttf'))
    c = canvas.Canvas("./Diplomas/DiplomasOrganizadores/Diploma-Organizador-"+apellidos+"-"+nombre+".pdf", pagesize=landscape(A4))
    c.drawImage("./resources/images/Diploma Organizador.jpg", 0, 0, width = 11.6 * inch, height = 8.4 * inch)
    c.setFont('Philosopher', 27)
    c.setTitle('Diploma - ' + nombre + apellidos)
    c.drawCentredString(5.75 * inch, 4.7 * inch, (nombre))
    c.drawCentredString(5.75 * inch, 4.1 * inch, (apellidos))
    c.drawCentredString(4.2 * inch, 3.55 * inch, (comite))
    c.drawCentredString(5.75 * inch, 1.9 * inch, (time.strftime("%d/%m/%y")))
    c.save()

def diplomasGeneradorOrganizador():
    
    filename = filedialog.askopenfilename(initialdir = pathlib.Path().absolute(),title = "Seleccione el fichero con los datos de organización",filetypes = [("Excel files", "*.xlsx")])
    df = pd.read_excel(filename,  header=None)
    contador = organizadorAuxiliar(df)
    messagebox.showinfo("Diplomas creados","Se han creado un total de " + str(contador) + " diplomas de organizador. Se han almacenado en /Diplomas/DiplomasOrganizador")

def organizadorAuxiliar(dataFrame):
    numero_filas = dataFrame.shape[0]
    contador = 0

    for i in range (1,numero_filas):

        columna = dataFrame.iloc[i].values
        comite = columna[7]
        apellidos = columna[1]   
        nombre = columna[2]
        
        if isinstance(comite, str) and isinstance(nombre, str) and isinstance(apellidos, str):
            pdfAutomaticoOrganizador(nombre, apellidos, comite)

        else:
            continue
        contador = contador + 1
    return contador