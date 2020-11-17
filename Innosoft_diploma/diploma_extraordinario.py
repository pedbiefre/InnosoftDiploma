#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import time
from tkinter import *

from reportlab.lib.pagesizes import landscape, A4, inch
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont

from Innosoft_diploma.diploma_ponente import *


def processPDFExcepcional(nombre, apellidos,motivo,fecha):
  c = canvas.Canvas("/home/blackylyzard/Formulario.pdf", pagesize=landscape(A4))
  c.drawImage("/home/blackylyzard/Descargas/DiplomaExcepcional.jpg", 0, 0, width = 11.6 * inch, height = 8.4 * inch)
  c.setFont('Helvetica', 30)
  c.drawCentredString(5.75 * inch, 4.7 * inch, (str(nombre.get())))
  c.drawCentredString(5.75 * inch, 4.1 * inch, (str(apellidos.get())))
  c.drawCentredString(5.75 * inch, 3 * inch, (str(motivo.get())))
  c.drawCentredString(5.75 * inch, 1.9 * inch, (str(fecha.get())))
  c.save()

#*****************NO BORRAR*****************
#PARA LINUX: os.system("evince /home/diego123/Escritorio/Formulario.pdf &")  
#PARA WINDOWS: os.system("start AcroRD32 ruta_y_archivo.pdf &")
  
  os.system("evince /home/blackylyzard/Formulario.pdf")

def diplomasExt():
  wind1 = Toplevel()

  nombre = StringVar()
  apellidos = StringVar()
  motivo = StringVar()
  fecha = StringVar(wind1, value=time.strftime("%d/%m/%y"))


  label = Label(wind1, text="Nombre")
  label.grid(row=0, column=0, sticky=W, padx=5, pady=5)

  entry = Entry(wind1, textvariable=nombre)
  entry.grid(row=0, column=1, padx=5, pady=5)

  label2 = Label(wind1, text="Apellidos")
  label2.grid(row=1, column=0, sticky=W, padx=5, pady=5)

  entry2 = Entry(wind1, textvariable=apellidos)
  entry2.grid(row=1, column=1, padx=5, pady=5)

  label3 = Label(wind1, text="Motivo")
  label3.grid(row=2, column=0, sticky=W, padx=5, pady=5)

  entry3 = Entry(wind1, textvariable=motivo)
  entry3.grid(row=2, column=1, padx=5, pady=5)

  label4 = Label(wind1, text="Fecha")
  label4.grid(row=3, column=0, sticky=W, padx=5, pady=5)

  entry4 = Entry(wind1, textvariable=fecha)
  entry4.grid(row=3, column=1, padx=5, pady=5)


  boton = Button(wind1, text="Procesar", command=lambda:processPDFExcepcional(nombre, apellidos, motivo, fecha))
  boton.grid(row=4, column=2)



def mainInterface():
  root = Tk()
  Button(root, text="Diplomas Asistencia", command=None).pack()

  Button(root, text="Diplomas Ponentes", command=diplomasPon).pack()
  Button(root, text="Diplomas Extraordinarios", command=diplomasExt).pack()

  root.mainloop()



  
 
if __name__ == "__main__":
  mainInterface()
 #TO DO: INICIAR LA VENTANA TKINTER CON ENTRADAS DE TEXTO Y UN BOTON CON LLAMADA AL METODO generarPDF()
 #app = QtGui.QApplication(sys.argv)
 #MyWindow = MyWindowClass(None)
 #MyWindow.show()
 #app.exec_()
