import pandas as pd
import sys
import os
import time
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import math

from reportlab.lib.pagesizes import landscape, A4, inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont

def pdfAutomatico(nombre, apellidos,eventos_asistidos,horas_totales):
    
    
    pdfmetrics.registerFont(TTFont('Philosopher', './resources/fonts/Philosopher-Italic.ttf'))
    c = canvas.Canvas("./Diplomas/DiplomasAutomaticos/Diploma-"+apellidos+"-"+nombre+".pdf", pagesize=landscape(A4))
    c.drawImage("./resources/images/Diploma Automatico.jpg", 0, 0, width = 11.6 * inch, height = 8.4 * inch)
    c.setFont('Philosopher', 27)
    c.setTitle('Diploma - ' + nombre.get() + apellidos.get())
    c.drawCentredString(5.75 * inch, 4.7 * inch, (nombre))
    c.drawCentredString(5.75 * inch, 4.1 * inch, (apellidos))
    c.drawCentredString(4.2 * inch, 3.55 * inch, (str(eventos_asistidos)))
    c.drawCentredString(6.8 * inch, 2.9 * inch, (str(horas_totales)))
    c.drawCentredString(5.75 * inch, 1.9 * inch, (time.strftime("%d/%m/%y")))
    c.save()

def diplomasGenerador():

    filename = filedialog.askopenfilename(initialdir = "/",title = "Seleccione el fichero con los datos de asistencia",filetypes = [("Excel files", "*.xlsx")])
    df = pd.read_excel(filename,  header=None)
    numero_filas = df.shape[0]
    contador = 0
    for i in range (1,numero_filas):
        
        columna = df.iloc[i].values
        apellidos = columna[1]   
        nombre = columna[2]
        eventos_asistidos = columna[10]
        horas_totales = columna[17]

        if horas_totales <= 1 or math.isnan(horas_totales):
            continue
        pdfAutomatico(nombre, apellidos, eventos_asistidos, horas_totales)
        contador = contador + 1
    messagebox.showinfo("Diplomas creados","Se han creado un total de " + str(contador) + " diplomas de asistencia. Se han almacenado en /Diplomas/DiplomasAutomaticos")

        