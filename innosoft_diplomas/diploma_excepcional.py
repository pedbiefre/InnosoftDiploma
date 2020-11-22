#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import time
from tkinter import *
from tkinter import messagebox

from reportlab.lib.pagesizes import landscape, A4, inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont

def processPDFExcepcional(nombre, apellidos,motivo,fecha,tipo):
  pdfmetrics.registerFont(TTFont('Philosopher', './resources/fonts/Philosopher-Italic.ttf'))

  if (tipo == "extraordinario"):
      path = "./Diplomas/DiplomasExcepcionales/Diploma Extraordinario "
      resource = "./resources/images/Diploma Extraordinario.jpg"
      title = 'Diploma Extraordinario - '
  if (tipo == "ponente"):
      path = "./Diplomas/DiplomasPonentes/Diploma Ponente "
      resource = "./resources/images/Diploma Ponente.jpg"
      title = 'Diploma Ponente - '
  if (tipo == "organizador"):
      path = "./Diplomas/DiplomasOrganizadores/Diploma Organizador "
      resource = "./resources/images/Diploma Organizador.jpg"
      title = 'Diploma Organizador - '

  c = canvas.Canvas(path + str(apellidos.get()) + "-" + str(nombre.get()) + ".pdf", pagesize=landscape(A4))
  c.drawImage(resource, 0, 0, width = 11.6 * inch, height = 8.4 * inch)
  c.setFont('Philosopher', 27)
  c.setTitle(title + nombre.get() + apellidos.get())
  c.drawCentredString(5.75 * inch, 4.7 * inch, (str(nombre.get())))
  c.drawCentredString(5.75 * inch, 4.1 * inch, (str(apellidos.get())))
  c.drawCentredString(5.75 * inch, 3 * inch, (str(motivo.get())))
  c.drawCentredString(5.75 * inch, 1.9 * inch, (str(fecha.get())))
  c.save()
  path = os.path.abspath(path + str(apellidos.get()) + "-" + str(nombre.get()) + ".pdf")
  messagebox.showinfo("Diploma creado","El diploma se ha generado correctamente en " + path)


def diplomasExc(tipo):
  wind1 = Toplevel()
  if(tipo=="extraordinario"):
    wind1.title("Diploma Extraordinario")
  if (tipo == "ponente"):
      wind1.title("Diploma Ponente")
  if (tipo == "organizador"):
      wind1.title("Diploma Organizador")

  nombre = StringVar()
  apellidos = StringVar()
  motivo = StringVar()
  fecha = StringVar(wind1, value=time.strftime("%d/%m/%y"))


  label = Label(wind1, text="Nombre")
  label.grid(row=0, column=0, sticky=W, padx=5, pady=5)

  entry = Entry(wind1, textvariable=nombre)
  entry.grid(row=0, column=1, padx=5, pady=5, ipadx=25)

  label2 = Label(wind1, text="Apellidos")
  label2.grid(row=1, column=0, sticky=W, padx=5, pady=5)

  entry2 = Entry(wind1, textvariable=apellidos)
  entry2.grid(row=1, column=1, padx=5, pady=5, ipadx=25)

  if (tipo == "ponente" or tipo == "organizador"):
      label3 = Label(wind1, text="Jornadas")
      label3.grid(row=2, column=0, sticky=W, padx=5, pady=5)
  else:
      label3 = Label(wind1, text="Motivo")
      label3.grid(row=2, column=0, sticky=W, padx=5, pady=5)

  entry3 = Entry(wind1, textvariable=motivo)
  entry3.grid(row=2, column=1, padx=5, pady=5, ipadx=25)

  label4 = Label(wind1, text="Fecha")
  label4.grid(row=3, column=0, sticky=W, padx=5, pady=5)

  entry4 = Entry(wind1, textvariable=fecha)
  entry4.grid(row=3, column=1, padx=5, pady=10, ipadx=25)


  boton = Button(wind1, text="Procesar", command=lambda:processPDFExcepcional(nombre, apellidos, motivo, fecha, tipo))
  boton.grid(row=5, column=0)
  wind1.geometry('290x160')
  wind1.iconbitmap("./resources/images/innosoft.ico")
