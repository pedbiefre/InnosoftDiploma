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
            diplomasGeneradorAsistencia(opcion.get())
    

    root = Toplevel()
    root.title("Innosoft Diplomas")
    root.geometry('600x600')

    title_label = Label(root,text="Título:").grid(row=3,column=0,sticky='e')
    title_entry = Entry(root)
    title_entry.grid(row=3,column=1,padx=2, pady=2, sticky='we', columnspan=9)

    subtitle_label = Label(root,text="Subtítulo:").grid(row=4,column=0,sticky='e')
    subtitle_entry = Entry(root)
    subtitle_entry.grid(row=4,column=1,padx=2, pady=2, sticky='we', columnspan=9)

    info_label = Label(root,text="Información:").grid(row=5,column=0,sticky='e')
    info_entry = Entry(root)
    info_entry.grid(row=5,column=1,padx=2, pady=2, sticky='we', columnspan=1)

    fecha = StringVar(root, value=time.strftime("%d/%m/%y"))
    date_label = Label(root,text="Fecha:").grid(row=6,column=0,sticky='e')
    date_entry = Entry(root,textvariable=fecha)
    date_entry.grid(row=6,column=1,padx=2, pady=2, sticky='we', columnspan=1)

    src_label = Label(root,text="Plantilla:").grid(row=7,column=0,sticky='e')
    src_entry = Entry(root)
    src_entry.grid(row=7,column=1,padx=2, pady=2, sticky='we', columnspan=9)
    
    entries = []
    entries.append(title_entry)
    entries.append(subtitle_entry)
    entries.append(info_entry)
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

    generar=Button(root, text="Generar", command=generar)
    generar.grid(row=8,column=5)
    

def pdfAutomaticoAsistenciaCustom(nombre, apellidos, eventos_asistidos, horas_totales,parametros):
    return 0

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

def diplomasGeneradorAsistencia(control):
    filename = filedialog.askopenfilename(initialdir = pathlib.Path().absolute(),title = "Seleccione el fichero con los datos de asistencia",filetypes = [("Excel files", "*.xlsx")])
    df = pd.read_excel(filename,  header=None)
    contador = asistenciaAuxiliar(df,control)
    messagebox.showinfo("Diplomas creados","Se han creado un total de " + str(contador) + " diplomas de asistencia. Se han almacenado en /Diplomas/DiplomasAsistencia")
    

def asistenciaAuxiliar(dataFrame,control):
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
            pdfAutomaticoAsistenciaCustom(nombre, apellidos, eventos_asistidos, horas_totales)
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