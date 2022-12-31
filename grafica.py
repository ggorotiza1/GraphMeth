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

    def xd(self,frame):
        frame2.place(x=100, y=0)
        #label.config(bg="#383838", fg="white", font=("Bahnschrift", 24))
        lbl_titulo.place(x=500, y=10)

        frame2.place(x=0, y=70)
        # radio1.place(x=0, y=2)
        # radio1.config(bg="#424141")
        # radio2.place(x=200, y=2)
        # radio2.config(bg="#424141")
        cmb_metodos.place(x=190, y=5)
        textoCombo = customtkinter.CTkLabel(frame, text="Seleccione un Método: ")
        textoCombo.place(x=10, y=1)

        frame1.place(x=0, y=100)
        lbl_formula.place(x=335, y=25)
        #titulo.config(font=("Bahnschrift", 18), bg="#5c5c5c", fg="white")
        lbl_intervaloA.place(x=260, y=165)
        #intervaloA.config(font=("Bahnschrift", 12), bg="#5c5c5c", fg="white")
        lbl_intervaloB.place(x=440, y=165)
        #intervaloB.config(font=("Bahnschrift", 12), bg="#5c5c5c", fg="white")
        txt_formula.place(x=333, y=65)
        txt_intervaloA.place(x=280, y=195)
        txt_intervaloB.place(x=460, y=195)
        btn_calcular.place(x=80, y=50)
        btn_graficar.place(x=80, y=110)
        btn_limpiar.place(x=80, y=170)
        lbl_rango.place(x=390, y=95)
        #l1.config(font=("Bahnschrift", 14), bg="#5c5c5c", fg="white")
        txt_rango.place(x=333, y=125)
        #lbl_img1.place(x=30, y=50)
        #lbl_img1.config(bg="#5c5c5c")
        #lbl_img2.place(x=30, y=110)
        #lbl_img2.config(bg="#5c5c5c")
        #lbl_img3.place(x=30, y=170)
        #lbl_img3.config(bg="#5c5c5c")
        #lbl_img4.place(x=550, y=120)
        #lbl_img4.config(bg="#5c5c5c")
        #Hovertip(lbl_img4, text="¿Qué valor ingresar?\nRepresentará el eje de las Abscisas.\nPor ejemplo: -20,20", hover_delay=500)

    def frameTabla(self, frame, label, trv):
        frame.place(x=0, y=350)
        #label.config(font=("Bahnschrift", 18), bg="#5c5c5c", fg="white")
        label.place(x=210, y=10)

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
        trv.place(x=20, y=60)

        textoAutores = customtkinter.CTkLabel(master=frame, text="Desarrollado por: Gorotiza - García - Masache")
        textoAutores.place(x=170, y=300)

    def frameGrafica(self, frame, label):
        frame.place(x=640, y=100)
        label.place(x=100, y=200)

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
            Metodos.dibujarEjes(cvs, frame4, lbl_grafica, tlb)
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

    def abrirPDF(event):
        path = 'ManualDeUsuario.pdf'
        os.system(path)

    def colorFondo():
        #wind = root
        #wind.config(bg="#ffffff")
        frame1.config(bg="#ffffff")
        lbl_formula.config(font=("Bahnschrift", 18), bg="#ffffff", fg="black")
        lbl_intervaloA.config(font=("Bahnschrift", 12), bg="#ffffff", fg="black")
        lbl_intervaloB.config(font=("Bahnschrift", 12), bg="#ffffff", fg="black")
        lbl_rango.config(font=("Bahnschrift", 14), bg="#ffffff", fg="black")
        txt_formula.config(bg="#000000", fg="white")
        txt_intervaloA.config(bg="#000000", fg="white")
        txt_intervaloB.config(bg="#000000", fg="white")
        txt_rango.config(bg="#000000", fg="white")
        btn_calcular.config(bg="#ffffff", fg="black")
        btn_graficar.config(bg="#ffffff", fg="black")
        btn_limpiar.config(bg="#ffffff", fg="black")
        lbl_img1.config(bg="#ffffff",image=img5)
        lbl_img2.config(bg="#ffffff",image=img6)
        #lbl_img3.config(bg="#ffffff",image=img7)
        #lbl_img4.config(bg="#ffffff",image=img8)
        #txt_intervaloA.config(font=("Bahnschrift", 12), bg="#000000", fg="white")
        #txt_intervaloB.config(font=("Bahnschrift", 12), bg="#000000", fg="white")
        #txt_rango.config(font=("Bahnschrift", 14), bg="#000000", fg="white")

    def accionesARealizar():
        if cmb_metodos.current() == -1:
            messagebox.showinfo("Atención",
                                "Seleccione un Método")
        elif cmb_metodos.current() == 0:
            # messagebox.showinfo("Hola", "Método de Bisección")
            Metodos.métodoDeBisección()
        elif cmb_metodos.current() == 1:
            # messagebox.showinfo("Hola", "Método de Falsa Posición")
            Metodos.métodoDeFalsaPosicion()
        elif cmb_metodos.current() == 2:
            #Metodos.métodoDeNewtonRaphson()
            Metodos.abrirPDF()

if __name__ == "__main__":
    root = customtkinter.CTk()

    # Frames Creados
    frame = customtkinter.CTkFrame(master = root, width=1280, height=70)  # Titulo
    frame1 = customtkinter.CTkFrame(master = root, width=1280, height=70)  # Formula
    frame2 = customtkinter.CTkFrame(master = root, width=640, height=250)  # Opciones
    frame3 = customtkinter.CTkFrame(master = root, width=640, height=370)  # Tabla
    frame4 = customtkinter.CTkFrame(master = root, width=640, height=620)  # Grafica

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
    lbl_titulo = customtkinter.CTkLabel(master = frame, text="Métodos Numéricos")
    lbl_formula = customtkinter.CTkLabel(master =frame1, text="Ingrese Fórmula")
    lbl_intervaloA = customtkinter.CTkLabel(master =frame1, text="Ingrese Intervalo [Xa]")
    lbl_intervaloB = customtkinter.CTkLabel(master =frame1, text="Ingrese Intervalo [Xb]")
    lbl_table = customtkinter.CTkLabel(master =frame3, text="Tabla de Resultados")
    lbl_grafica = customtkinter.CTkLabel(master =frame4, text="Gráfica")
    #lbl_img1 = customtkinter.CTkLabel(master =frame1, image=img1)
    #lbl_img2 = customtkinter.CTkLabel(master =frame1, image=img2)
    #lbl_img3 = customtkinter.CTkLabel(master =frame1, image=img3)
    #lbl_img4 = customtkinter.CTkLabel(master =frame1, image=img4)
    # Para la Grafica
    lbl_rango = customtkinter.CTkLabel(master =frame1, text="Rango")
    txt_rango = customtkinter.CTkLabel(master =frame1)
#    txt_rango.insert(0,"-20,20")

    # Entrys Creados
    txt_formula = customtkinter.CTkEntry(master =frame1)
    txt_intervaloA = customtkinter.CTkEntry(master =frame1)
    txt_intervaloB = customtkinter.CTkEntry(master =frame1)

    # Radios Creados
    rbt_biseccion = Radiobutton(frame2, text="Método de Bisección")
    rbt_falsaposicion = Radiobutton(
        frame2, text="Método de Falsa Posición")

    # Combobox creados
    cmb_metodos = customtkinter.CTkComboBox(master = frame2, values=["Método de Bisección", "Método de Falsa Posición", "Método de Newton-Raphson"])
    # cmb_metodos.bind("<<ComboboxSelected>>", Metodos.accionesARealizar)

    # Tabla Creada
    trv = ttk.Treeview(frame3, columns=("i", "xa", "xb", "xr", "ea(%)"))

    # Grafica
    cvs = FigureCanvasTkAgg(fig, frame4)
    tlb = NavigationToolbar2Tk(cvs, frame4)


    # Buttons Creados
    btn_calcular = customtkinter.CTkButton(master=frame1, text="Calcular", command=Metodos.accionesARealizar)
    btn_graficar = customtkinter.CTkButton(master=frame1, text="Graficar", command=Metodos.represent)
    btn_limpiar = customtkinter.CTkButton(master=frame1, text="Nuevo",command=Metodos.limpiar)
    btn_modo = customtkinter.CTkButton(master=frame, text="Modo", command=Metodos.colorFondo)
    btn_modo.place(x=900, y=0)
    
    # Inicialización de la Clase
    Metodos = Metodos(root)
    Metodos.xd(root)
    # Uso de Recursos

    # Metodos.dibujarEjes(cvs, frame4)

root.mainloop()
