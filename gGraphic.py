from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import numpy as np
from matplotlib import pyplot as plt
from math import *
from sympy import symbols
from sympy import lambdify
from sympy import sympify
import customtkinter

# Realizado por Gabriel Gorotiza
def graficar(
    formula: Entry, rangoAbcisasG: Entry, rangoOrdenadasG: Entry, frame: Frame
):
    global fig, canvas, toolbar

    # Si existe una figura y un canvas, los limpia y destruye antes de dibujar uno nuevo
    if "canvas" in globals():
        canvas.get_tk_widget().destroy()
        toolbar.destroy()

    # Verifica si la fórmula ingresada no está vacía
    if formula.get() == "":
        return  # Si está vacía, no hace nada
    else:
        # Procesa el rango de las abcisas (eje x)
        rangoAbcisas = rangoAbcisasG.get().split(",")
        lmin = float(rangoAbcisas[0])
        lmax = float(rangoAbcisas[1])

        # Procesa el rango de las ordenadas (eje y)
        rangoOrdenadas = rangoOrdenadasG.get().split(",")
        lmin1 = float(rangoOrdenadas[0])
        lmax1 = float(rangoOrdenadas[1])

        # Crea los puntos del eje x
        xpts = np.arange(lmin, lmax, 0.1)

        # Define el símbolo y la función
        x = symbols("x")
        fn = sympify(formula.get())
        f = lambdify(x, fn, "numpy")

        # Crea la figura del gráfico
        fig = plt.figure()
        plt.plot(xpts, f(xpts), label=fn)
        plt.legend(loc="upper right")
        plt.axhline(color="#6f6f6f")
        plt.axvline(color="#6f6f6f")
        plt.grid(True, which="both")
        plt.xlabel("Abscisas", color="#318DC8")
        plt.ylabel("Ordenadas", color="#318DC8")
        plt.ylim(lmin1, lmax1)

        # Integra el gráfico en el frame de Tkinter
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()
        toolbar = NavigationToolbar2Tk(canvas, frame)
        toolbar.update()
        canvas.get_tk_widget().pack(
            side=customtkinter.TOP, fill=customtkinter.BOTH, expand=True
        )


def eliminarGrafica():
    fig.clf()
    canvas.get_tk_widget().destroy()
    toolbar.destroy()
    canvas.draw()
