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
from PIL import Image
import customtkinter
# from scipy.misc import derivative
import matplotlib
matplotlib.use("TkAgg")


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
fun = {"sin:": "np.sin", "cos": "np.cos", "tan": "nap.tan",
       "sqrt": "np.sqrt", "exp": "np.exp", "log": "np.log", "pi": "np.pi"}

vocales = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
           "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "x", "y", "z"}
act_rango = False
ul_ran = ""
ran = ""


# Estilos de la Gráfica
# style.use('fivethirtyeight')
# style.use('dark_background')
style.use('seaborn-v0_8-pastel')
# style.use('Solarize_Light2')
# style.use('ggplot')


class Metodos:
    def __init__(self, root):
        self.wind = root
        self.wind.title("GraphMeth - Métodos Cerrados - Cuarto 'A'")
        self.wind.geometry("1280x720")
        self.wind.resizable(0, 0)
        self.wind.iconbitmap("Recursos/GraphMeth2.0.ico")

    def métodoDeBisección(event):
        txt1 = txt_formula.get()
        txt2 = txt_intervaloA.get()
        txt3 = txt_intervaloB.get()
        if txt1 != "" and txt2 != "" and txt3 != "":
            formula = txt_formula.get()
            x = symbols('x')
            fn = sympify(formula)
            f = lambdify(x, fn, "numpy")

            a = float(txt_intervaloA.get())
            b = float(txt_intervaloB.get())
            crit = 0.0000001
            i = 0
            ea = 1
            x_anterior = 0

            while ea > crit:
                xr = (a+b)/2
                ea = abs((xr-x_anterior)/xr)

                if (f(xr) * f(a)) < 0:
                    b = xr
                else:
                    a = xr
                x_anterior = xr
                trv.insert("", END, values=(i, a, b, x_anterior, (ea*100)))
                i = i + 1
            ax.scatter(xr, 0, c="red")

        else:
            messagebox.showinfo("Atención", "Debe llenar todos los campos")

    def métodoDeFalsaPosicion(event):
        txt1 = txt_formula.get()
        txt2 = txt_intervaloA.get()
        txt3 = txt_intervaloB.get()

        if txt1 != "" and txt2 != "" and txt3 != "":
            formula = txt_formula.get()
            x = symbols('x')
            fn = sympify(formula)
            f = lambdify(x, fn, "numpy")

            a = float(txt_intervaloA.get())
            b = float(txt_intervaloB.get())
            crit = 0.0000001
            i = -1
            xr_anterior = 0
            xr = (a*f(b) - b*f(a)) / (f(b) - f(a))

            ea = abs(xr-xr_anterior)

            while ea > crit:
                xr_anterior = (a*f(b) - b*f(a)) / (f(b) - f(a))
                if f(a) * f(b) >= 0:
                    messagebox.showinfo("Error", "Error")
                    quit()
                elif f(xr_anterior) * f(a) < 0:
                    ea = abs(xr_anterior - b)
                    b = xr_anterior
                    i = i+1
                elif f(xr_anterior) * f(b) < 0:
                    ea = abs(xr_anterior - a)
                    a = xr_anterior
                    i = i+1
                else:
                    messagebox.showinfo("Error", "Error")
                trv.insert("", END, values=(i, a, b, xr_anterior, ea))
            ax.scatter(xr, 0, c="red")
        else:
            messagebox.showinfo("Atención", "Debe llenar todos los campos")

    def graficar():
        global ax
        global canvas
        global toolbar
        rann = txt_rango.get()
        ran = rann.split(",")
        lmin = float(ran[0])
        lmax = float(ran[1])
        xpts = np.arange(lmin, lmax, 0.1)
        formula = txt_formula.get()
        x = symbols('x')
        fn = sympify(formula)
        f = lambdify(x, fn)

        fig = Figure(figsize=(6, 5), dpi=100)

        canvas = FigureCanvasTkAgg(fig, master=frame2)
        ax = fig.add_subplot(111)
        ax.plot(xpts, f(xpts), label=fn, color="#006666")
        ax.axhline(0, color="#6f6f6f")
        ax.axvline(0, color="#6f6f6f")
        ax.grid(True, which='both')
        ax.legend(loc='upper right')
        
        canvas.draw()

        toolbar = NavigationToolbar2Tk(canvas, frame2)
        toolbar.update()

        canvas.get_tk_widget().pack(side=customtkinter.TOP,
                                    fill=customtkinter.BOTH, expand=True)

    def limpiar():
        txt_formula.delete(0, END)
        txt_intervaloA.delete(0, END)
        txt_intervaloB.delete(0, END)
        trv.delete(*trv.get_children())
        ax.clear()
        canvas.get_tk_widget().destroy()
        toolbar.destroy()
        canvas.draw()
        

    def accionesARealizar():
        if cmb_metodos.get() == "":
            messagebox.showinfo("Atención",
                                "Seleccione un Método")
        elif cmb_metodos.get() == "Método de Bisección":
            # messagebox.showinfo("Hola", "Método de Bisección")
            Metodos.métodoDeBisección()
        elif cmb_metodos.get() == "Método de Falsa Posición":
            # messagebox.showinfo("Hola", "Método de Falsa Posición")
            Metodos.métodoDeFalsaPosicion()
        elif cmb_metodos.get() == "Método de Newton-Raphson":
            Metodos.métodoDeNewtonRaphson()

    def change_appearance_mode_event(new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)


if __name__ == "__main__":
    root = customtkinter.CTk()

    # Frames Creados
    frame = customtkinter.CTkFrame(
        master=root, width=1280, height=720)
    frame.place(x=0, y=0)

    frame2 = customtkinter.CTkFrame(
        master=root, width=640, height=720, bg_color="#ffffff")
    frame2.place(x=640, y=100)

    # Entry
    txt_rango = customtkinter.CTkEntry(master=frame, font=(
        "Roboto", 15), width=180, justify="center")
    txt_rango.place(x=340, y=240)
    txt_rango.insert(END, "-20,20")
    txt_formula = customtkinter.CTkEntry(master=frame, font=(
        "Roboto", 15), width=180, justify="center", placeholder_text="Ej: sin(x)", border_width=2)
    txt_formula.place(x=340, y=170)
    txt_intervaloA = customtkinter.CTkEntry(master=frame, font=(
        "Roboto", 15), width=140, justify="center", placeholder_text="Ej: -1 o 0", border_width=2)
    txt_intervaloA.place(x=280, y=320)
    txt_intervaloB = customtkinter.CTkEntry(master=frame, font=(
        "Roboto", 15), width=140, justify="center", placeholder_text="Ej: 0 o 1", border_width=2)
    txt_intervaloB.place(x=450, y=320)
    textoAutores = customtkinter.CTkLabel(
        master=frame, text="Desarrollado por: Gorotiza - García - Masache", font=("Roboto", 16))
    textoAutores.place(x=155, y=660)

    # Imagenes
    img1 = customtkinter.CTkImage(light_image=Image.open("Recursos/calculadora1.png"),
                                  dark_image=Image.open(
                                      "Recursos/calculadora.png"),
                                  size=(36, 36))
    img2 = customtkinter.CTkImage(light_image=Image.open("Recursos/grafica1.png"),
                                  dark_image=Image.open(
                                      "Recursos/grafica.png"),
                                  size=(36, 36))
    img3 = customtkinter.CTkImage(light_image=Image.open("Recursos/limpiar1.png"),
                                  dark_image=Image.open(
                                      "Recursos/limpiar.png"),
                                  size=(36, 36))
    img4 = customtkinter.CTkImage(light_image=Image.open("Recursos/info1.png"),
                                  dark_image=Image.open("Recursos/info.png"),
                                  size=(24, 24))
    img5 = customtkinter.CTkImage(light_image=Image.open("Recursos/tema1.png"),
                                  dark_image=Image.open("Recursos/tema.png"),
                                  size=(24, 24))

    # Labels Creados
    lbl_img1 = customtkinter.CTkLabel(frame, image=img1, text="")
    lbl_img1.place(x=30, y=163)
    lbl_img2 = customtkinter.CTkLabel(frame, image=img2, text="")
    lbl_img2.place(x=30, y=223)
    lbl_img3 = customtkinter.CTkLabel(frame, image=img3, text="")
    lbl_img3.place(x=30, y=283)
    lbl_img4 = customtkinter.CTkLabel(frame, image=img4, text="")
    lbl_img4.place(x=540, y=210)
    lbl_img5 = customtkinter.CTkLabel(frame, image=img5, text="")
    lbl_img5.place(x=960, y=19)
    Hovertip(lbl_img4, text="¿Qué valor ingresar?\nRepresentará el eje de las abscisas.\nPor ejemplo: -20,20", hover_delay=500)

    lbl_titulo = customtkinter.CTkLabel(
        master=frame, text="Métodos Numéricos", font=("Roboto", 25))
    lbl_titulo.place(x=530, y=15)
    lbl_formula = customtkinter.CTkLabel(
        master=frame, text="Ingrese Fórmula", font=("Roboto", 20))
    lbl_formula.place(x=360, y=130)
    lbl_intervaloA = customtkinter.CTkLabel(
        master=frame, text="Ingrese Intervalo [Xa]", font=("Roboto", 15))
    lbl_intervaloA.place(x=280, y=280)
    lbl_intervaloB = customtkinter.CTkLabel(
        master=frame, text="Ingrese Intervalo [Xb]", font=("Roboto", 15))
    lbl_intervaloB.place(x=450, y=280)
    lbl_table = customtkinter.CTkLabel(
        master=frame, text="Tabla de Resultados", font=("Roboto", 24))
    lbl_table.place(x=230, y=370)
    lbl_grafica = customtkinter.CTkLabel(
        master=frame2, text="Gráfica", font=("Roboto", 24))
    lbl_grafica.pack(pady=10)
    lbl_rango = customtkinter.CTkLabel(
        master=frame, text="Rango", font=("Roboto", 20))
    lbl_rango.place(x=400, y=210)
    lbl_combo = customtkinter.CTkLabel(
        master=frame, text="Seleccione un Método:", font=("Roboto", 14))
    lbl_combo.place(x=10, y=60)

    # Combobox
    cmb_metodos = customtkinter.CTkComboBox(master=frame, values=[
                                            "", "Método de Bisección", "Método de Falsa Posición"], width=220)
    cmb_metodos.place(x=170, y=60)

    # Tabla Creada
    style = ttk.Style()

    # Estilos de Tabla 'clam', 'alt', 'default', 'classic'
    style.theme_use('alt')
    style.configure("Treeview.Heading", background="#424141",
                    foreground="white", fieldbackground="black")
    trv = ttk.Treeview(frame, columns=("i", "xa", "xb", "xr", "ea(%)"))
    trv.column("#0", width=0, anchor=CENTER)
    trv.column("i", width=80, anchor=CENTER)
    trv.column("xa", width=80, anchor=CENTER)
    trv.column("xb", width=80, anchor=CENTER)
    trv.column("xr", width=80, anchor=CENTER)
    trv.column("ea(%)", width=80, anchor=CENTER)

    trv.heading("#0", text="", anchor=CENTER)
    trv.heading("i", text="i", anchor=CENTER)
    trv.heading("xa", text="Xa", anchor=CENTER)
    trv.heading("xb", text="Xb", anchor=CENTER)
    trv.heading("xr", text="Xr", anchor=CENTER)
    trv.heading("ea(%)", text="Ea(%)", anchor=CENTER)
    trv.place(x=20, y=410, width=600)

    # Buttons Creados
    btn_calcular = customtkinter.CTkButton(master=frame, text="Calcular", width=150, height=40, font=(
        "Roboto", 16), command=Metodos.accionesARealizar, border_width=2)
    btn_calcular.place(x=80, y=160)
    btn_graficar = customtkinter.CTkButton(master=frame, text="Graficar", width=150, height=40, font=(
        "Roboto", 16), command=Metodos.graficar, border_width=2)
    btn_graficar.place(x=80, y=220)
    btn_limpiar = customtkinter.CTkButton(master=frame, text="Nuevo", width=150, height=40, font=(
        "Roboto", 16), command=Metodos.limpiar, border_width=2)
    btn_limpiar.place(x=80, y=280)

    # ComboBox Creado
    cmb_modo = customtkinter.CTkOptionMenu(master=frame, values=[
                                           "System", "Dark", "Light", ], width=220, command=Metodos.change_appearance_mode_event)
    cmb_modo.place(x=1000, y=20)

    # Inicialización de la Clase
    Metodos = Metodos(root)

root.mainloop()
