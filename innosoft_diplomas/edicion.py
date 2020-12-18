#!/usr/bin/python
from tkinter import Toplevel, StringVar, Label, W, Entry, ttk, Button, OptionMenu
import tkinter as tk


from innosoft_diplomas import parametros


def actualizarParametros(parametros, fuente):
    parametros.set_fuente(fuente)



def selecFuente(parametros):
    wind1 = Toplevel()
    wind1.title('Edición')


    label = Label(wind1, text="Fuente")
    label.grid(row=0, column=0, sticky=W, padx=5, pady=5)

    OptionList = [
        "Philosopher",
        "Abecedary",
        "Gemini",
        "Cancer"
    ]

    entry = tk.Spinbox(wind1, values=list(OptionList))
    entry.grid(row=1, column=1)


    def seleccionarFuente(parametros):
        parametros.set_fuente(entry.get())
        print(parametros.get_fuente())


    boton = Button(wind1, text="Aceptar",
    command=lambda: seleccionarFuente(parametros))
    boton.grid(row=2, column=2)
