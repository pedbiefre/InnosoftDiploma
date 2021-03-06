import pandas as pd
import smtplib
import os.path

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from validate_email import validate_email

from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import pathlib

from tkinter import *
from functools import partial
import math

def sendEmails(username, password):
    filename = peticionArchivo()
    file = pd.read_excel(filename)
    destinatarios = file['Correo']
    nombres = file["Nombre"]
    apellidos = file["Apellidos"]
    horas_totales = file["Horas en total"]

    usuarioAuxiliar(username)
    passwordAuxiliar(password)
    destinatariosAuxiliar(destinatarios)
    nombresAuxiliar(nombres)
    apellidosAuxiliar(apellidos)


    remitente = username
    asunto = "Diploma jornadas Innosoft"
    body = "En este correo se le adjunta su diploma de acreditación de las jornadas Innosoft."

    # Creamos la conexión con el servidor
    sesion_smtp = smtplib.SMTP('smtp.gmail.com', 587)

    # Ciframos la conexión
    sesion_smtp.starttls()

    # Iniciamos sesión en el servidor
    sesion_smtp.login(username, password)

    for i in range(len(destinatarios)):
        horas = float(horas_totales[i])
        if not(horas is not math.nan and horas > 0 ):
            continue

        path = './Diplomas/DiplomasAsistencia/Diploma-Asistente-' + apellidos[i] + '-' + nombres[i] + '.pdf'
        file_name = "Diploma-" + apellidos[i].replace(" ", "") + '-' + nombres[i].replace(" ", "") + '.pdf'
        diplomaPDF(path)

        # Creamos el objeto mensaje
        mensaje = MIMEMultipart()

        # Establecemos los atributos del mensaje
        mensaje['From'] = remitente
        mensaje['To'] = destinatarios[i]
        mensaje['Subject'] = asunto

        # Agregamos el cuerpo del mensaje como objeto MIME de tipo texto
        mensaje.attach(MIMEText(body, 'plain'))

        # Abrimos el archivo que vamos a adjuntar
        archivo_adjunto = open(path, 'rb')

        # Creamos un objeto MIME base
        adjunto_MIME = MIMEBase('application', 'octet-stream')
        # Y le cargamos el archivo adjunto
        adjunto_MIME.set_payload(archivo_adjunto.read())
        # Codificamos el objeto en BASE64
        encoders.encode_base64(adjunto_MIME)
        # Agregamos una cabecera al objeto
        aux = "attachment; filename=" + file_name
        adjunto_MIME.add_header('Content-Disposition', aux)
        # Y finalmente lo agregamos al mensaje
        mensaje.attach(adjunto_MIME)

        # Convertimos el objeto mensaje a texto
        texto = mensaje.as_string()

        # Enviamos el mensaje
        sesion_smtp.sendmail(remitente, destinatarios[i], texto)

    # Cerramos la conexión
    sesion_smtp.quit()
    messagebox.showinfo("Se han enviado los correos correctamente.")

def peticionArchivo():
    filename = filedialog.askopenfilename(initialdir=pathlib.Path().absolute(),
                                          title="Seleccione el fichero con los datos de asistencia",
                                          filetypes=[("Excel files", "*.xlsx")])
    return filename

def login():
    # window
    tkWindow = Toplevel()
    tkWindow.geometry('400x150')
    tkWindow.title('Email Login Form')

    # username label and text entry box
    usernameLabel = Label(tkWindow, text="Email address").grid(row=0, column=0)
    username = StringVar()
    usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)

    # password label and password entry box
    passwordLabel = Label(tkWindow, text="Password").grid(row=1, column=0)
    password = StringVar()
    passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)

    # login button
    loginButton = Button(tkWindow, text="Login", command=lambda: [sendEmails(username.get(), password.get()), tkWindow.destroy()]).grid(row=4, column=0)


def nombresAuxiliar(nombres):
    contador = 0
    for line in nombres:
        if line != '':
            contador = contador + 1
    return contador

def apellidosAuxiliar(apellidos):
    contador = 0
    for line in apellidos:
        if isinstance(line, str):
            contador = contador + 1
    return contador

def usuarioAuxiliar(usuario):
    contador = 0
    if validate_email(email=usuario, check_mx=False):
        contador = contador + 1
    return contador

def passwordAuxiliar(password):
    contador = 0
    if password:
        contador = contador + 1
    return contador

def diplomaPDF(path):
    contador = 0
    if os.path.isfile(path):
        contador = contador + 1
    return contador

def validar_email_aux(email):
    return validate_email(email=email, check_mx=False)

def destinatariosAuxiliar(destinatarios):
    contador = 0
    for line in destinatarios:
        if line != "":
            contador = contador + 1
    return contador