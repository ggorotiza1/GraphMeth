from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import numpy as np
from matplotlib import pyplot as plt
from math import *
from sympy import symbols
from sympy import lambdify
from sympy import sympify
import customtkinter
# Realizado por Gabriel Gorotiza, Gabriel García, Blade Masache


def graficar(formula: Entry, rangoAbcisasG: Entry, rangoOrdenadasG: Entry, frame: Frame):
    global fig, canvas, toolbar
    if formula.get() == "":
        pass
    else:
        rangoAbcisas = rangoAbcisasG.get().split(",")
        lmin = float(rangoAbcisas[0])
        lmax = float(rangoAbcisas[1])
        rangoOrdenadas = rangoOrdenadasG.get().split(",")
        lmin1 = float(rangoOrdenadas[0])
        lmax1 = float(rangoOrdenadas[1])
        xpts = np.arange(lmin, lmax, 0.1)
        x = symbols('x')
        fn = sympify(formula.get())
        f = lambdify(x, fn, "numpy")

        fig = plt.figure()
        plt.plot(xpts, f(xpts), label=fn)
        plt.legend(loc='upper right')
        plt.axhline(color="#6f6f6f")
        plt.axvline(color="#6f6f6f")
        plt.grid(True, which='both')
        plt.xlabel("Abscisas", color="#318DC8")
        plt.ylabel("Ordenadas", color="#318DC8")
        plt.ylim(lmin1, lmax1)

        canvas = FigureCanvasTkAgg(fig, master=frame)

        canvas.draw()
        toolbar = NavigationToolbar2Tk(canvas, frame)
        toolbar.update()

        canvas.get_tk_widget().pack(side=customtkinter.TOP,
                                    fill=customtkinter.BOTH, expand=True)


def eliminarGrafica():
    fig.clf()
    canvas.get_tk_widget().destroy()
    toolbar.destroy()
    canvas.draw()
