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
customtkinter.set_default_color_theme("dark-blue")
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
        self.wind.resizable(0, 0)
        self.wind.iconbitmap("Icono_GraphMeth.ico")
        
    def dibujarEjes(self, cvs, frame, lb, tlb):
        cvs.get_tk_widget().pack_forget()  # Por revisar eliminación de la grafica
        lb.pack(side=TOP, fill=BOTH, expand=1)
        cvs.draw()
        cvs.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
        tlb.update()
       

    def reemplaza(self, p):
        for i in fun:
            if i in p:
                p = p.replace(i, fun[i])
            return p

    def animate(i):
        global act_rango
        global ul_ran
        if act_rango == True:
            try:
                lmin = float(ran[0])
                lmax = float(ran[1])
                if lmin < lmax:
                    x = np.arange(lmin, lmax, .01)  # .01
                    ul_ran = [lmin, lmax]
                else:
                    act_rango = False
            except:
                messagebox.showwarning(
                    "Error", "Introduzca los valores del rango de x, separado por coma.")
                act_rango = False
                txt_rango.delete(0, len(txt_rango.get()))
        else:
            if ul_ran != "":
                x = np.arange(ul_ran[0], ul_ran[1], .01)  # .01
            else:
                x = np.arange(1, 10, .01)  # .01
        try:
            solo = f(x)
            ax1.clear()

            formula = txt_formula.get()
            textoTitulo = ""
            fn = sympify(formula)

            textoTitulo = fn

            ax1.plot(x, solo, label=textoTitulo, color="#006666")
            ax1.legend(loc='upper right')
            ax1.xlabel('Eje de las Abcisas')
            ax1.ylabel('Eje de las Ordenadas')
        except:
            ax1.plot()
        ax1.axhline(0, color="#6f6f6f")
        ax1.axvline(0, color="#6f6f6f")
        Metodos.ani.event_source.stop()  # DETIENE ANIMACIÓN

    def represent():
        global graph_data
        global ran
        global act_rango
        global f
        formula = txt_formula.get()
        rangotex = txt_rango.get()

        if formula != "" and rangotex != "":
            x = symbols('x')
            fn = sympify(formula)
            f = lambdify(x, fn, "numpy")
            print("funcion: ", str(fn))

            if txt_rango.get() != "":
                rann = txt_rango.get()
                ran = rann.split(",")
                act_rango = True
            #graph_data = f(x)
            Metodos.ani.event_source.start()  # INICIA/REANUDA ANIMACIÓN
            Metodos.dibujarEjes(cvs, frame, lbl_grafica, tlb)
        else:
            messagebox.showwarning("Atención", "Falta Fórmula o Rango")

    ani = animation.FuncAnimation(fig, animate, interval=10)
    plt.show()

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
            crit = 0.00000001
            i = 0
            ea = 1
            x_anterior = 0

            while ea > crit:
                xr = (a+b)/2
                ea = abs((xr-x_anterior)/xr)

                if f(xr) * f(a) < 0:
                    b = xr
                else:
                    a = xr
                x_anterior = xr
                trv.insert("", END, values=(i, a, b, xr, (ea*100)))
                i = i + 1
            ax1.scatter(xr, 0, c="red")

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
            crit = 0.00000001
            i = 0
            x_anterior = 0
            ea = 100
            while ea > crit:
                xr = b - (f(b) * (a - b) / (f(a) - f(b)))
                ea = ((xr - x_anterior) / xr) * 100
                prod = f(xr) * f(a)
                if prod < 0:
                    b = xr
                else:
                    a = xr
                # xold stores the previous value of xr to find absolute error.
                x_anterior = xr
                trv.insert("", END, values=(i, a, b, xr, ea))
                i = i+1
            ax1.scatter(xr, 0, c="red")
        else:
            messagebox.showinfo("Atención", "Debe llenar todos los campos")

    def métodoDeNewtonRaphson(event):
        formula = txt_formula.get()
        xi = txt_intervaloA.get()
        x = symbols('x')
        fn = sympify(formula)
        fx = lambdify(x, fn, "numpy")

        yprima = fn.diff(x)
        yp = sympify(yprima)
        fdx = lambdify(x, yprima, "numpy")

        ea=100
        i=0
        crit = 0.00001
        while ea > crit:
            xr = xi-(fx(xi)/fdx(xi))
            ea=abs((xr-xi)/xr)*100

            xi=xr

        messagebox("resultado: " , xr)

    def limpiar():
        global trv
        global cvs
        txt_formula.delete(0, END)
        txt_intervaloA.delete(0, END)
        txt_intervaloB.delete(0, END)
        trv.delete(*trv.get_children())

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

    def change_appearance_mode_event(new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)
    

if __name__ == "__main__":
    root = customtkinter.CTk()

    # Frames Creados
    frame = customtkinter.CTkFrame(master = root, width=1280, height=720)  # Titulo
    frame.place(x=0, y=0)

    frame2 = customtkinter.CTkFrame(master = root, width=640, height=720, bg_color="#ffffff")  # Titulo
    frame2.place(x=640, y=100)

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
    lbl_intervaloA.place(x=280, y=280)
    lbl_intervaloB = customtkinter.CTkLabel(master =frame, text="Ingrese Intervalo [Xb]", font=("Roboto",15))
    lbl_intervaloB.place(x=450, y=280)
    lbl_table = customtkinter.CTkLabel(master =frame, text="Tabla de Resultados", font=("Roboto",24))
    lbl_table.place(x=230, y=370)
    lbl_grafica = customtkinter.CTkLabel(master =frame2, text="Gráfica", font=("Roboto", 24))
    #lbl_img1 = customtkinter.CTkLabel(master =frame1, image=img1)
    #lbl_img2 = customtkinter.CTkLabel(master =frame1, image=img2)
    #lbl_img3 = customtkinter.CTkLabel(master =frame1, image=img3)
    #lbl_img4 = customtkinter.CTkLabel(master =frame1, image=img4)
    # Para la Grafica
    lbl_rango = customtkinter.CTkLabel(master =frame, text="Rango", font=("Roboto", 20))
    lbl_rango.place(x=400, y=210)
    txt_rango = customtkinter.CTkEntry(master =frame, font=("Roboto", 15), width=180, justify="center")
    txt_rango.place(x=340, y=240)
    txt_rango.insert(END, "-20,20")
#    txt_rango.insert(0,"-20,20")

    # Entrys Creados
    txt_formula = customtkinter.CTkEntry(master =frame, font=("Roboto", 15), width=180, justify="center", placeholder_text="Ej: sin(x)")
    txt_formula.place(x=340, y=170)
    txt_intervaloA = customtkinter.CTkEntry(master =frame, font=("Roboto", 15), width=140, justify="center", placeholder_text="Ej: -1 o 0")
    txt_intervaloA.place(x=280, y=320)
    txt_intervaloB = customtkinter.CTkEntry(master =frame, font=("Roboto", 15), width=140, justify="center", placeholder_text="Ej: 0 o 1")
    txt_intervaloB.place(x=450, y=320)
    textoAutores = customtkinter.CTkLabel(master=frame, text="Desarrollado por: Gorotiza - García - Masache", font=("Roboto", 16))
    textoAutores.place(x=155, y=660)

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
    style = ttk.Style()
    style.theme_use('alt')
    # 'clam', 'alt', 'default', 'classic'
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
    btn_calcular = customtkinter.CTkButton(master=frame, text="Calcular", width=150, height=40, font=("Roboto", 16), command=Metodos.accionesARealizar)
    btn_calcular.place(x=80, y=160)
    btn_graficar = customtkinter.CTkButton(master=frame, text="Graficar", width=150, height=40, font=("Roboto", 16), command=Metodos.represent)
    btn_graficar.place(x=80, y=220)
    btn_limpiar = customtkinter.CTkButton(master=frame, text="Nuevo", width=150, height=40, font=("Roboto", 16), command=Metodos.limpiar)
    btn_limpiar.place(x=80, y=280)

    cmb_modo = customtkinter.CTkOptionMenu(master=frame, values=["Dark", "Light", "System"], width=220, command=Metodos.change_appearance_mode_event)
    cmb_modo.place(x=1000, y=20)


    # Grafica
    cvs = FigureCanvasTkAgg(fig, frame2)
    #cvs.get_tk_widget().place(x = 640, y = 100)
    tlb = NavigationToolbar2Tk(cvs, frame2)
    # Inicialización de la Clase
    Metodos = Metodos(root)



root.mainloop()
