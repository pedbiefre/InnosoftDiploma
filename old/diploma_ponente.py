import sys
import os
import time
from tkinter import *
from tkinter import messagebox


from reportlab.lib.pagesizes import landscape, A4, inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont

#Función que llama a la generación de diplomas de ponentes
def processPDFPonente(nombre, apellidos, motivo, fecha):
    #Se define la fuente a usar en el diploma
    pdfmetrics.registerFont(TTFont('Philosopher', './resources/fonts/Philosopher-Italic.ttf'))
    c = canvas.Canvas("./Diplomas/DiplomasPonentes/Diploma Ponente " + str(apellidos.get()) + "-" + str(nombre.get()) + ".pdf", pagesize=landscape(A4))
    #Se define la plantilla a usar en el diploma
    c.drawImage("./resources/images/Diploma Ponente.jpg", 0, 0, width=11.6 * inch, height=8.4 * inch)
    c.setFont('Philosopher', 27)
    c.setTitle('Diploma Ponente - ' + nombre.get() + apellidos.get())
    #con drawCentredString se define la posición de los elementos sobre la plantilla
    c.drawCentredString(5.75 * inch, 4.7 * inch, (str(nombre.get())))
    c.drawCentredString(5.75 * inch, 4.1 * inch, (str(apellidos.get())))
    c.drawCentredString(5.75 * inch, 3 * inch, (str(motivo.get())))
    c.drawCentredString(5.75 * inch, 1.9 * inch, (str(fecha.get())))
    #Se guarda el diploma
    c.save()
    #Se muestra un mensaje que indica que se ha generado correctamente el diploma en la ruta marcada
    path = os.path.abspath("./Diplomas/DiplomasPonentes/Diploma Ponente " + str(apellidos.get()) + "-" + str(nombre.get()) + ".pdf")
    messagebox.showinfo("Diploma creado","El diploma se ha generado correctamente en " + path)



def diplomasPon():
  wind1 = Toplevel()
  wind1.title("Diploma Ponente")

  nombre = StringVar()
  apellidos = StringVar()
  motivo = StringVar()
  fecha = StringVar(wind1, value=time.strftime("%d/%m/%y"))

  # Se define la localización de cada uno de los parámetros del diploma en la ventana de Tkinter
  label = Label(wind1, text="Nombre")
  label.grid(row=0, column=0, sticky=W, padx=5, pady=5)

  entry = Entry(wind1, textvariable=nombre)
  entry.grid(row=0, column=1, padx=5, pady=5, ipadx=25)

  label2 = Label(wind1, text="Apellidos")
  label2.grid(row=1, column=0, sticky=W, padx=5, pady=5)

  entry2 = Entry(wind1, textvariable=apellidos)
  entry2.grid(row=1, column=1, padx=5, pady=5, ipadx=25)

  label3 = Label(wind1, text="Motivo")
  label3.grid(row=2, column=0, sticky=W, padx=5, pady=5)

  entry3 = Text(wind1, height = 10, width = 25)
  entry3.pack

  label4 = Label(wind1, text="Fecha")
  label4.grid(row=3, column=0, sticky=W, padx=5, pady=5)

  entry4 = Entry(wind1, textvariable=fecha)
  entry4.grid(row=3, column=1, padx=5, pady=10, ipadx=25)

  #Al pulsar en Procesar se llama a la función processPDFExcepcional() la cual procede a generar el diploma
  boton = Button(wind1, text="Procesar", command=lambda: processPDFExcepcional(nombre, apellidos, entry3, fecha))
  boton.grid(row=5, column=0)
  wind1.geometry('290x160')
  wind1.iconbitmap("./resources/images/innosoft.ico")
