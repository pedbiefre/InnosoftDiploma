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
    root.geometry('500x500')

    opcion = IntVar()

    radio1 = Radiobutton(root, text="BÁSICO", variable=opcion, 
            value=1)
    radio2 = Radiobutton(root, text="CUSTOM", variable=opcion, 
            value=2)

    radio1.pack()
    radio2.pack()

    title_label = Label(root,text="Title")
    title_entry = Entry(root)
    title_entry.pack()
    title_label.pack()

    generar=Button(root, text="Generar", command=generar)
    generar.pack()

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