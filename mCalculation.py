from tkinter import messagebox
import numpy as np
from math import *
from sympy import symbols
from sympy import lambdify
from sympy import sympify
import sympy as sp
import customtkinter
from tkinter import *
from tkinter import ttk
from matplotlib import pyplot


def métodoDeBisección(
    formula: Entry,
    txt2: Entry,
    txt3: Entry,
    trv: ttk.Treeview,
    plt: pyplot,
    frame: Frame,
):
    """
    Implements the Bisection Method to find the root of a function within a given interval.

    Args:
        formula (Entry): The input field for the mathematical formula.
        txt2 (Entry): The input field for the lower bound of the interval.
        txt3 (Entry): The input field for the upper bound of the interval.
        trv (ttk.Treeview): The Treeview widget to display the iteration results.
        plt (pyplot): The pyplot object for plotting the graph.
        frame (Frame): The frame to display the result label.

    Returns:
        None
    """
    global lbl_resultado
    global xr
    if formula.get() != None and txt2.get() != None and txt3.get() != None:
        formula = formula.get()
        x = symbols("x")
        fn = sympify(formula)
        f = lambdify(x, fn, "numpy")
        crit = 0.0000001
        i = 0
        ea = 1
        xr_anterior = 0
        try:
            a = float(txt2.get())
            b = float(txt3.get())
            if f(a) * f(b) >= 0:  
                messagebox.showerror("Error", "¡Error! Fuera de Rango")
            else:
                while ea > crit:
                    xr = (a + b) / 2
                    ea = abs((xr - xr_anterior) / xr)
                    if (f(xr) * f(a)) < 0:
                        b = xr
                    else:
                        a = xr
                    xr_anterior = xr
                    trv.insert("", END, values=(i, a, b, xr_anterior, (ea * 100)))
                    i = i + 1
                plt.scatter(xr, 0, c="red")
                # plt.annotate(xr_anterior, xy=(xr_anterior, 3.5))
                lbl_resultado = customtkinter.CTkLabel(
                    master=frame,
                    text="Raíz encontrada en: " + str(xr_anterior),
                    font=("Roboto", 12),
                )
                lbl_resultado.place(x=220, y=640)

        except ValueError:
            messagebox.showwarning("Atención", "Los intervalos deben ser números")
    else:
        messagebox.showinfo("Atención", "Debe llenar todos los campos")


def métodoDeFalsaPosicion(
    formula: Entry,
    txt2: Entry,
    txt3: Entry,
    trv: ttk.Treeview,
    plt: pyplot,
    frame: Frame,
):
    """
    Implements the method of false position to find the root of a function within a given interval.

    Args:
        formula (Entry): The input field for the mathematical formula.
        txt2 (Entry): The input field for the lower bound of the interval.
        txt3 (Entry): The input field for the upper bound of the interval.
        trv (ttk.Treeview): The treeview widget to display the iteration results.
        plt (pyplot): The pyplot object for plotting.
        frame (Frame): The frame widget to display the result label.

    Returns:
        None
    """
    global lbl_resultado
    if formula != None and txt2 != None and txt3 != None:
        formula = formula.get()
        x = symbols("x")
        fn = sympify(formula)
        f = lambdify(x, fn, "numpy")

        a = float(txt2.get())
        b = float(txt3.get())
        crit = 0.0000001
        i = -1
        xr_anterior = 0
        xr = (a * f(b) - b * f(a)) / (f(b) - f(a))

        ea = abs(xr - xr_anterior)
        try:
            a = float(txt2.get())
            b = float(txt3.get())
            if f(a) * f(b) >= 0:  # Revisar el fuera de rango
                messagebox.showerror("Error", "¡Error! Fuera de Rango")
            else:
                while ea > crit:
                    xr_anterior = (a * f(b) - b * f(a)) / (f(b) - f(a))
                    if f(xr_anterior) * f(a) < 0:
                        ea = abs(xr_anterior - b)
                        b = xr_anterior
                        i = i + 1
                    elif f(xr_anterior) * f(b) < 0:
                        ea = abs(xr_anterior - a)
                        a = xr_anterior
                        i = i + 1
                    else:
                        messagebox.showinfo("Error", "Error")
                    trv.insert("", END, values=(i, a, b, xr_anterior, ea))
                plt.scatter(xr_anterior, 0, c="red")
                # plt.annotate(xr_anterior, xy=(xr_anterior, 3.5))
                lbl_resultado = customtkinter.CTkLabel(
                    master=frame,
                    text="Raíz encontrada en: " + str(xr_anterior),
                    font=("Roboto", 12),
                )
                lbl_resultado.place(x=220, y=640)
        except ValueError:
            messagebox.showwarning("Atención", "Los intervalos deben ser números")
    else:
        messagebox.showinfo("Atención", "Debe llenar todos los campos")


def eliminarLabel():
    """
    This function checks if the label 'lbl_resultado' exists and destroys it if it does.
    """
    if lbl_resultado.winfo_exists():
        lbl_resultado.destroy()
    else:
        pass
