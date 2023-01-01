from tkinter import ttk
from tkinter import *
from tkinter import Button as tk_btn
from tkinter import messagebox
from matplotlib.pyplot import *
from matplotlib.figure import Figure
from matplotlib import style
import matplotlib.animation as anim
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.animation as animation
from math import *
from sympy import symbols
from sympy import lambdify
from sympy import sympify
from idlelib.tooltip import Hovertip
import sympy as sp
import os
import customtkinter
# from scipy.misc import derivative

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")
fun = {"sin:": "np.sin", "cos": "np.cos", "tan": "nap.tan",
       "sqrt": "np.sqrt", "exp": "np.exp", "log": "np.log", "pi": "np.pi"}

vocales = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
           "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "x", "y", "z"}
act_rango = False
ul_ran = ""
ran = ""
fig = Figure()
# style.use('fivethirtyeight')
# style.use('dark_background')
# style.use('seaborn-v0_8-pastel')
style.use('Solarize_Light2')
# style.use('ggplot')
ax1 = fig.add_subplot(111)


class Metodos:
    def __init__(self, root):
        self.wind = root
        self.wind.title("GraphMeth - Métodos Cerrados - Cuarto 'A'")
        self.wind.geometry("1280x720")
        #self.wind.config(bg="#383838")
        #self.wind.resizable(0, 0)
        self.wind.iconbitmap("Icono_GraphMeth.ico")
        
    def change_appearance_mode_event(new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)
    

if __name__ == "__main__":
    root = customtkinter.CTk()

    # Frames Creados
    frame = customtkinter.CTkFrame(master = root, width=1280, height=720)  # Titulo
    frame.place(x=0, y=0)

    # Imagenes
    img1 = PhotoImage(file="calculadora.png")
    img2 = PhotoImage(file="grafica.png")
    img3 = PhotoImage(file="limpiar.png")
    img4 = PhotoImage(file="info.png")
    img5 = PhotoImage(file="calculadora1.png")
    img6 = PhotoImage(file="grafica1.png")
    img7 = PhotoImage(file="limpiar1.png")
    img8 = PhotoImage(file="info1.png")

    # Labels Creados
    lbl_titulo = customtkinter.CTkLabel(master = frame, text="Métodos Numéricos", font=("Roboto",25))
    lbl_titulo.place(x=530, y=15)
    lbl_formula = customtkinter.CTkLabel(master =frame, text="Ingrese Fórmula", font=("Roboto",20))
    lbl_formula.place(x=360,y=130)
    lbl_intervaloA = customtkinter.CTkLabel(master =frame, text="Ingrese Intervalo [Xa]", font=("Roboto",15))
    lbl_intervaloA.place(x=280, y=220)
    lbl_intervaloB = customtkinter.CTkLabel(master =frame, text="Ingrese Intervalo [Xb]", font=("Roboto",15))
    lbl_intervaloB.place(x=450, y=220)
    lbl_table = customtkinter.CTkLabel(master =frame, text="Tabla de Resultados", font=("Roboto",24))
    lbl_table.place(x=230, y=330)
    lbl_grafica = customtkinter.CTkLabel(master =frame, text="Gráfica")
    #lbl_img1 = customtkinter.CTkLabel(master =frame1, image=img1)
    #lbl_img2 = customtkinter.CTkLabel(master =frame1, image=img2)
    #lbl_img3 = customtkinter.CTkLabel(master =frame1, image=img3)
    #lbl_img4 = customtkinter.CTkLabel(master =frame1, image=img4)
    # Para la Grafica
    lbl_rango = customtkinter.CTkLabel(master =frame, text="Rango")
    txt_rango = customtkinter.CTkLabel(master =frame)
#    txt_rango.insert(0,"-20,20")

    # Entrys Creados
    txt_formula = customtkinter.CTkEntry(master =frame, font=("Roboto", 15), width=180, justify="center")
    txt_formula.place(x=340, y=170)
    txt_intervaloA = customtkinter.CTkEntry(master =frame, font=("Roboto", 15), width=140, justify="center")
    txt_intervaloA.place(x=280, y=260)
    txt_intervaloB = customtkinter.CTkEntry(master =frame, font=("Roboto", 15), width=140, justify="center")
    txt_intervaloB.place(x=450, y=260)

    # Radios Creados
    rbt_biseccion = Radiobutton(frame, text="Método de Bisección")
    rbt_falsaposicion = Radiobutton(
        frame, text="Método de Falsa Posición")

    # Combobox creados
    lbl_combo = customtkinter.CTkLabel(master =frame, text="Seleccione un Método:", font=("Roboto",14))
    lbl_combo.place(x=10, y=60)
    cmb_metodos = customtkinter.CTkComboBox(master = frame, values=["Método de Bisección", "Método de Falsa Posición", "Método de Newton-Raphson"], width=220)
    cmb_metodos.place(x=170, y=60)
    # cmb_metodos.bind("<<ComboboxSelected>>", Metodos.accionesARealizar)

    # Tabla Creada
    trv = ttk.Treeview(frame, columns=("i", "xa", "xb", "xr", "ea(%)"))

    # Buttons Creados
    btn_calcular = customtkinter.CTkButton(master=frame, text="Calcular", width=150, height=40, font=("Roboto", 16))
    btn_calcular.place(x=80, y=140)
    btn_graficar = customtkinter.CTkButton(master=frame, text="Graficar", width=150, height=40, font=("Roboto", 16))
    btn_graficar.place(x=80, y=200)
    btn_limpiar = customtkinter.CTkButton(master=frame, text="Nuevo", width=150, height=40, font=("Roboto", 16))
    btn_limpiar.place(x=80, y=260)

    cmb_modo = customtkinter.CTkOptionMenu(master=frame, values=["Dark", "Light", "System"], width=220, command=Metodos.change_appearance_mode_event)
    cmb_modo.place(x=900, y=0)

    # Inicialización de la Clase
    Metodos = Metodos(root)



root.mainloop()
