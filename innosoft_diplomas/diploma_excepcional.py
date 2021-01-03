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


def processPDFExcepcional(nombre, apellidos,motivo,fecha,tipo, parametros):

  def auxInitParams(nombre, apellidos,motivo,fecha):
      res = []
      apellidos = str(apellidos.get())
      nombre = str(nombre.get())
      motivo = str(motivo.get())
      fecha = str(fecha.get())
      res.append(nombre)
      res.append(apellidos)
      res.append(motivo)
      res.append(fecha)
      return res

  if (tipo == "extraordinario"):
      path = "./Diplomas/DiplomasExcepcionales/Diploma Extraordinario "
      resource = "./resources/images/Diploma Extraordinario.jpg"
      data = auxInitParams(nombre, apellidos, motivo, fecha)
      title = 'Diploma Extraordinario - '
  if (tipo == "ponente"):
      path = "./Diplomas/DiplomasPonentes/Diploma Ponente "
      resource = "./resources/images/Diploma Ponente.jpg"
      title = 'Diploma Ponente - '
      data = auxInitParams(nombre, apellidos, motivo, fecha)
  if (tipo == "organizador"):
      path = "./Diplomas/DiplomasOrganizadores/Diploma Organizador "
      resource = "./resources/images/Diploma Organizador.jpg"
      title = 'Diploma Organizador - '
      data = auxInitParams(nombre, apellidos, motivo, fecha)
  if (tipo == "extraordinarioTEST"):

      path = "./InnosoftDiploma/Diplomas/DiplomasExcepcionales/Diploma Extraordinario "
      resource = "./InnosoftDiploma/resources/images/Diploma Extraordinario.jpg"
      title = 'Diploma Extraordinario - '
      data = []
      data.append(nombre)
      data.append(apellidos)
      data.append(motivo)
      data.append(fecha)

  if (tipo == "ponenteTEST"):
      path = "./Diplomas/DiplomasPonentes/Diploma Ponente "
      resource = "./resources/images/Diploma Ponente.jpg"
      title = 'Diploma Ponente - '
      data = []
      data.append(nombre)
      data.append(apellidos)
      data.append(motivo)
      data.append(fecha)

  if (tipo == "organizadorTEST"):
      path = "./Diplomas/DiplomasPonentes/Diploma Organizador "
      resource = "./resources/images/Diploma Organizador.jpg"
      title = 'Diploma Organizador - '
      data = []
      data.append(nombre)
      data.append(apellidos)
      data.append(motivo)
      data.append(fecha)

  c = canvas.Canvas(path + data[1] + "-" + data[0]  + ".pdf", pagesize=landscape(A4))
  c.drawImage(resource, 0, 0, width = 11.6 * inch, height = 8.4 * inch)

  if parametros.get_fuente() == 'Philosopher':
    pdfmetrics.registerFont(TTFont('Philosopher', './resources/fonts/Philosopher-Italic.ttf'))
    c.setFont('Philosopher', 27)
  elif parametros.get_fuente() == 'Abecedary':
    pdfmetrics.registerFont(TTFont('Abecedary', './resources/fonts/Abecedary Italic.ttf'))
    c.setFont('Abecedary', 27)
  elif parametros.get_fuente() == 'AndikaNewBasic':
    pdfmetrics.registerFont(TTFont('AndikaNewBasic', './resources/fonts/AndikaNewBasic-I.ttf'))
    c.setFont('AndikaNewBasic', 27)

  c.setTitle(title + data[0] + data[1])
  c.drawCentredString(5.75 * inch, 4.7 * inch, (data[0]))
  c.drawCentredString(5.75 * inch, 4.1 * inch, (data[1]))
  c.drawCentredString(5.75 * inch, 3 * inch, (data[2]))
  c.drawCentredString(5.75 * inch, 1.9 * inch, (data[3]))
  c.save()
  path = os.path.abspath(path + data[1] + "-" + data[0] + ".pdf")
  if (tipo[-4:] != 'TEST'):
      messagebox.showinfo("Diploma creado","El diploma se ha generado correctamente en " + path)


def diplomasExc(tipo, parametros):
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


  boton = Button(wind1, text="Procesar", command=lambda:processPDFExcepcional(nombre, apellidos, motivo, fecha, tipo, parametros))
  boton.grid(row=5, column=0)
  wind1.geometry('290x160')
  wind1.iconbitmap("./resources/images/innosoft.ico")
