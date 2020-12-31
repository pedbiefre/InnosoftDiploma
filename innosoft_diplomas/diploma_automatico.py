import pandas as pd
import sys
import os
import time
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import math
import pathlib

from reportlab.lib.pagesizes import landscape, A4, inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont

def pdfAutomaticoAsistencia(nombre, apellidos,eventos_asistidos,horas_totales):
    
    
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

def diplomasGeneradorAsistencia():

    filename = filedialog.askopenfilename(initialdir = pathlib.Path().absolute(),title = "Seleccione el fichero con los datos de asistencia",filetypes = [("Excel files", "*.xlsx")])
    df = pd.read_excel(filename,  header=None)
    contador = asistenciaAuxiliar(df)
    messagebox.showinfo("Diplomas creados","Se han creado un total de " + str(contador) + " diplomas de asistencia. Se han almacenado en /Diplomas/DiplomasAsistencia")

def asistenciaAuxiliar(dataFrame):
    numero_filas = dataFrame.shape[0]
    contador = 0
    for i in range (1,numero_filas):
        
        columna = dataFrame.iloc[i].values
        apellidos = columna[1]   
        nombre = columna[2]
        eventos_asistidos = columna[10]
        horas_totales = columna[17]

        if not(isinstance(horas_totales, int)) or horas_totales <= 0 or  not(isinstance(nombre, str)) or not(isinstance(apellidos, str)) or not(isinstance(eventos_asistidos, int)):
            continue
        pdfAutomaticoAsistencia(nombre, apellidos, eventos_asistidos, horas_totales)
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