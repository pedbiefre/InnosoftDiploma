#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import time
from tkinter import *

from reportlab.pdfgen import canvas

def processPDF(nombre, apellidos,titulo,fecha):
  c = canvas.Canvas("/home/blackylyzard/Formulario.pdf")
  c.drawString(100, 750, "DIPLOMA EXTRAORDINARIO INNOSOFT")
  c.drawString(100, 700, ("Nombre: " + str(nombre.get())))
  c.drawString(100, 680, ("Apellidos: " + str(apellidos.get())))
  c.drawString(100, 660, ("Observaciones: " + str(titulo.get())))
  c.drawString(100, 620, ("Fecha: " + str(fecha.get())))
  c.save()

  os.system("evince /home/blackylyzard/Formulario.pdf")

def diplomasExt():
  wind1 = Toplevel()

  nombre = StringVar()
  apellidos = StringVar()
  titulo = StringVar()
  fecha = StringVar(wind1, value=time.strftime("%d/%m/%y"))


  label = Label(wind1, text="Nombre")
  label.grid(row=0, column=0, sticky=W, padx=5, pady=5)

  entry = Entry(wind1, textvariable=nombre)
  entry.grid(row=0, column=1, padx=5, pady=5)

  label2 = Label(wind1, text="Apellidos")
  label2.grid(row=1, column=0, sticky=W, padx=5, pady=5)

  entry2 = Entry(wind1, textvariable=apellidos)
  entry2.grid(row=1, column=1, padx=5, pady=5)

  label3 = Label(wind1, text="Título")
  label3.grid(row=2, column=0, sticky=W, padx=5, pady=5)

  entry3 = Entry(wind1, textvariable=titulo)
  entry3.grid(row=2, column=1, padx=5, pady=5)

  label4 = Label(wind1, text="Fecha")
  label4.grid(row=3, column=0, sticky=W, padx=5, pady=5)

  entry4 = Entry(wind1, textvariable=fecha)
  entry4.grid(row=3, column=1, padx=5, pady=5)


  boton = Button(wind1, text="Procesar", command=lambda:processPDF(nombre, apellidos, titulo, fecha))
  boton.grid(row=4, column=2)


def mainInterface():
  root = Tk()
  Button(root, text="Diplomas Asistencia", command=None).pack()

  Button(root, text="Diplomas Extraordinarios", command=diplomasExt).pack()

  root.mainloop()



  
 
if __name__ == "__main__":
  mainInterface()
 #TO DO: INICIAR LA VENTANA TKINTER CON ENTRADAS DE TEXTO Y UN BOTON CON LLAMADA AL METODO generarPDF()
 #app = QtGui.QApplication(sys.argv)
 #MyWindow = MyWindowClass(None)
 #MyWindow.show()
 #app.exec_()