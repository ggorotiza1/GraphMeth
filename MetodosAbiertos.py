from tkinter import ttk
from tkinter import *
import tkinter
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
from sympy import diff
from idlelib.tooltip import Hovertip
import sympy as sp
import os
from sympy import Derivative, diff, simplify
# from scipy.misc im


class Metodos:
    def __init__(self, root):
        self.wind = root
        self.wind.title("")
        self.wind.geometry("883x668")
        self.wind.config(bg="#383838")
        self.wind.resizable(0, 0)

    def metodoDeLaSecante(event):
        formula = entry1.get()
        x = symbols('x')
        fn = sympify(formula)
        f = lambdify(x, fn, "numpy")

        x0 = float(entry2.get())
        x1 = float(entry3.get())
        step = 1
        ea=1
        crit = 0.0000001
        tabla1 = ttk.Treeview(frame, columns=("i", "xi","ea(%)"))
        tabla1.column("#0", width=0, anchor=CENTER)
        tabla1.column("i", width=80, anchor=CENTER)
        tabla1.column("xi", width=80, anchor=CENTER)
        tabla1.column("ea(%)", width=80, anchor=CENTER)

        tabla1.heading("#0", text="", anchor=CENTER)
        tabla1.heading("i", text="i", anchor=CENTER)
        tabla1.heading("xi", text="Xa", anchor=CENTER)
        tabla1.heading("ea(%)", text="Ea(%)", anchor=CENTER)
        tabla1.place(x=150, y=410, width=600)
        while ea> crit:
            if f(x0) == f(x1):
                print('Divide by zero error!')
                break
        
            x2 = x0 - (x1-x0)*f(x0)/(f(x1) - f(x0))
            ea = abs(f(x2))
            tabla1.insert("", END, values=(step, x2,ea))

            #print('Iteration-%d, x2 = %0.6f and f(x2) = %0.6f' %
             #     (step, x2, f(x2)))
            x0 = x1
            x1 = x2
            step = step + 1

        labelResultado = Label(frame, text=f"Raiz: {x1}", font=(
            "Roboto", 10), foreground="#000000")
        labelResultado.place(x=300, y=280)

    def metodoNewtonRaphson(event):
        formula = entry1.get()
        x = symbols('x')
        fn = sympify(formula)
        f = lambdify(x, fn, "numpy")
        fp = Derivative(fn, x).doit()

        fprima = lambdify(x, fp, "numpy")

        x0 = float(entry2.get())
        crit = 0.0000001
        step = 1
        condition = True
        while condition:
            if fprima(x0) == 0.0:
                print('Divide by zero error!')
                break

            x1 = x0 - f(x0)/fprima(x0)
            print('Iteration-%d, x1 = %0.6f and f(x1) = %0.6f' %
                  (step, x1, f(x1)))
            x0 = x1
            step = step + 1

            condition = abs(f(x1)) > crit
            labelResultado = Label(frame, text=f"Raiz: {x1}", font=(
                "Roboto", 10), foreground="#000000")
            labelResultado.place(x=300, y=280)
        else:
            print('\nNot Convergent.')

    def accionesARealizar():
            if opcion1 == "Metodo de Newton-Raphson":
                Metodos.metodoNewtonRaphson()
            elif opcion1 == "Metodo de la Secante":
                Metodos.metodoDeLaSecante()

    def presentarEntrys(opcion: str):
        global opcion1
        global label2, label3, label4, entry2, entry3, entry4, tabla1
        opcion1 = opcion
        if opcion == "Metodo de Newton-Raphson":
            label4 = Label(frame, text="Ingrese Intervalo A",
                           font=("Roboto", 10), foreground="#000000")
            label4.place(x=220, y=190)
            entry4 = Entry(frame)
            entry4.place(x=220, y=220)
            label2.destroy()
            entry2.destroy()
            label3.destroy()
            entry3.destroy()
        elif opcion == "Metodo de la Secante":
            label2 = Label(frame, text="Ingrese Intervalo A",
                           font=("Roboto", 10), foreground="#000000")
            label2.place(x=220, y=190)
            entry2 = Entry(frame)
            entry2.place(x=220, y=220)
            label3 = Label(frame, text="Ingrese Intervalo B",
                           font=("Roboto", 10), foreground="#000000")
            label3.place(x=350, y=190)
            entry3 = Entry(frame)
            entry3.place(x=350, y=220)

            label4.destroy()
            entry4.destroy()

if __name__ == "__main__":
    root = Tk()
#exp(x)-(x^2)-(3*x)
    # Frames Creados
    frame = Frame(root, width=883, height=668, background="#ffffff")  # Titulo
    frame.place(x=0, y=0)

    img1 = PhotoImage(file="Recursos/fondo1.png")
    lbl_img1 = Label(frame, image=img1)
    lbl_img1.place(x=0, y=0)

    label1 = Label(frame, text="Ingrese Formula",
                   font=("Roboto", 10), foreground="#000000")
    label1.place(x=70, y=190)
    entry1 = Entry(frame)
    entry1.place(x=70, y=220)
    value_inside = tkinter.StringVar(root)
    btn_calcular = tk_btn(frame, text="Calcular", width=20,
                          height=2, command=Metodos.accionesARealizar, bg="#5c5c5c", fg="#ffffff", font=("Bahnschrift", 10), relief=SOLID)
    btn_calcular.place(x=150,y=320)
    # Set the default value of the variable
    value_inside.set("Seleccione una Opcion")
    options_list = ["Metodo de Newton-Raphson", "Metodo de la Secante", "Metodo de Punto Fijo"]
    cmb_metodos = OptionMenu(frame, value_inside, *options_list, command=Metodos.presentarEntrys)
    cmb_metodos.place(x=70, y=140)


    Metodos = Metodos(root)

root.mainloop()
