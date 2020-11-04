#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys
import os
from reportlab.pdfgen import canvas
#TODO ESTO VA A SER SUSTITUIDO POR TKINTER
#from PyQt5 import QtCore, QtGui, uic 
 
# Cargar nuestro archivo .ui
#form_class = uic.loadUiType("formularioPDF.ui")[0]
 
#class MyWindowClass(QtGui.QMainWindow, form_class):
 #def __init__(self, parent=None):
  #QtGui.QMainWindow.__init__(self, parent)
  #self.setupUi(self)
  
  #self.btn_pdf.clicked.connect(self.generarPDF)

  
 # Evento del boton btn_pdf
def generarPDF():
  
  # Guardo en las variables los datos de los textEdit Ingresados por el Usuario
  #self.nombre = str(self.textNombre.toPlainText())
  #self.apellido = str(self.textApellido.toPlainText())
  #self.correo = str(self.textCorreo.toPlainText())
  #self.curso = str(self.textCurso.toPlainText())
  #self.pais = str(self.textPais.toPlainText())
  #self.obs = str(self.textObs.toPlainText())
  
    
  # Ruta donde quiero crear el PDF
  c = canvas.Canvas("C:/Users/pbied/Desktop/Formulario.pdf")
  c.drawString(100,750,"DIPLOMA EXTRAORDINARIO INNOSOFT")
  c.drawString(100,700,("Nombre: "+ "Pedro"))
  c.drawString(100,680,("Apellidos: "+ "Biedma Fresno"))
  c.drawString(100,660,("Observaciones: "+ "Completo el reto de la jornada en el menor tiempo posible"))
  c.drawString(100,620,("Fecha: "+ "05/11/2020"))
 
  c.save()

  #PARA LINUX: os.system("evince /home/diego123/Escritorio/Formulario.pdf &")  
  #PARA WINDOWS: os.system("start AcroRD32 ruta_y_archivo.pdf &")
  os.system("start AcroRD32 C:/Users/pbied/Desktop/Formulario.pdf &") 
  
 
if __name__ == "__main__":
 #TO DO: INICIAR LA VENTANA TKINTER CON ENTRADAS DE TEXTO Y UN BOTON CON LLAMADA AL METODO generarPDF()
 #app = QtGui.QApplication(sys.argv)
 #MyWindow = MyWindowClass(None)
 #MyWindow.show()
 #app.exec_()
 generarPDF()