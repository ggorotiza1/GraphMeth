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
        self.wind.geometry("720x540")
        self.wind.config(bg="#383838")
        self.wind.resizable(0, 0)

    def metodoDeLaSecante():
        formula = entry1.get()
        x = symbols('x')
        fn = sympify(formula)
        f = lambdify(x, fn, "numpy")

        x0 = float(entry2.get())
        x1 = float(entry3.get())
        step = 1
        condition = True
        crit = 0.0000001
        while condition:
            if f(x0) == f(x1):
                print('Divide by zero error!')
                break

            x2 = x0 - (x1-x0)*f(x0)/(f(x1) - f(x0))
            print('Iteration-%d, x2 = %0.6f and f(x2) = %0.6f' %
                  (step, x2, f(x2)))
            x0 = x1
            x1 = x2
            step = step + 1
            condition = abs(f(x2)) > crit
        labelResultado = Label(frame, text=("Raiz: ", x2), font=(
            "Roboto", 10), foreground="#000000")
        labelResultado.place(x=300, y=10)

    def metodoNewtonRaphson():
        formula = entry1.get()
        x = symbols('x')
        fn = sympify(formula)
        f = lambdify(x, fn, "numpy")
        fp = Derivative(fn, x).doit()

        fprima=lambdify(x, fp, "numpy")

        x0 = float(entry2.get())
        crit = 0.0000001
        step = 1
        flag = 1
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
            labelResultado = Label(frame, text=("Raiz: ", x1), font=(
                "Roboto", 10), foreground="#000000")
            labelResultado.place(x=300, y=10)
        else:
            print('\nNot Convergent.')


if __name__ == "__main__":
    root = Tk()

    # Frames Creados
    frame = Frame(root, width=720, height=540, background="#ffffff")  # Titulo
    frame.place(x=0, y=0)

    label1 = Label(frame, text="Ingrese Formula",
                   font=("Roboto", 10), foreground="#000000")
    label1.place(x=10, y=10)
    entry1 = Entry(frame)
    entry1.place(x=10, y=30)

    label2 = Label(frame, text="Ingrese Intervalo A",
                   font=("Roboto", 10), foreground="#000000")
    label2.place(x=150, y=10)
    entry2 = Entry(frame)
    entry2.place(x=150, y=30)
    label3 = Label(frame, text="Ingrese Intervalo B",
                   font=("Roboto", 10), foreground="#000000")
    label3.place(x=150, y=60)
    entry3 = Entry(frame)
    entry3.place(x=150, y=80)
    button1 = tk_btn(frame, text="Calcular", width=20, background="#000000",
                     foreground="#ffffff", command=Metodos.metodoNewtonRaphson)
    button1.place(x=80, y=150)

    Metodos = Metodos(root)

root.mainloop()
