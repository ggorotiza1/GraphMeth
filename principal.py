from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from matplotlib.pyplot import *
from matplotlib import style
from matplotlib import pyplot as plt
from math import *
from idlelib.tooltip import Hovertip
from PIL import Image
import customtkinter
import matplotlib
import pygame
from gGraphic import graficar as grafico
from gGraphic import eliminarGrafica as eGrafico
from mCalculation import métodoDeFalsaPosicion as mFP
from mCalculation import métodoDeBisección as mB
from mCalculation import eliminarLabel as eL
from kFrame import createTeclado as cKeyboard
from kFrame import deleteTeclado as dKeyboard
from tButton import ToggleButton as toggle
import webbrowser

matplotlib.use("TkAgg")

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
act_rango = False
ul_ran = ""
ran = ""
plt.style.use("bmh")
bandera = False


class Metodos:
    """
    A class that represents the methods for GraphMeth.

    Attributes:
        wind: The root window of the application.
    """

    def __init__(self, root):
        """
        Initializes the Metodos class.

        Args:
            root: The root window of the application.
        """
        self.wind = root
        self.wind.title("GraphMeth - Métodos Cerrados - Cuarto 'A'")
        self.wind.geometry("1280x720+0+0")
        self.wind.resizable(0, 0)
        self.wind.iconbitmap("Recursos/GraphMeth2.0.ico")

    def accionesARealizar():
        """
        Performs the actions based on the selected method.

        Raises:
            messagebox.showinfo: If no method is selected.
        """
        if cmb_metodos.get() == "":
            messagebox.showinfo("Atención", "Seleccione un Método")
        elif cmb_metodos.get() == "Método de Bisección":
            # messagebox.showinfo("Hola", "Método de Bisección")
            mB(txt_formula, txt_intervaloA, txt_intervaloB, trv, plt, frame)
            reproducirSonido()

        elif cmb_metodos.get() == "Método de Falsa Posición":
            # messagebox.showinfo("Hola", "Método de Falsa Posición")
            mFP(txt_formula, txt_intervaloA, txt_intervaloB, trv, plt, frame)
            reproducirSonido()

    def change_appearance_mode_event(new_appearance_mode: str):
        """
        Changes the appearance mode of the application.

        Args:
            new_appearance_mode: The new appearance mode to be set.
        """
        customtkinter.set_appearance_mode(new_appearance_mode)

    def abrirManual():
        """
        Opens the user manual for GraphMeth.
        """
        reproducirSonido()
        path = "https://drive.google.com/file/d/173yvF9CMz0WXC5OGpmexOUrphuM_XC_5/view?usp=sharing"
        webbrowser.open_new(path)

        # archivo = open('Recursos/manual2.pdf', 'r')
        # archivo.read()

        # path = "Recursos/manualUsuario2.jpg"
        # im = Image.open(path)
        # im.show()


def click_boton(valor):
    """
    This function is called when a button is clicked.
    
    It plays a sound and inserts the given value into the text field.
    
    Parameters:
    - valor: The value to be inserted into the text field.
    """
    reproducirSonido()
    cont = len(txt_formula.get())
    txt_formula.insert(cont, valor)


def reproducirSonido():
    """
    Reproduce un sonido de fondo utilizando el archivo "uChatScrollButton.wav".
    """
    sonido_fondo = pygame.mixer.Sound("Sonidos/uChatScrollButton.wav")
    pygame.mixer.Sound.play(sonido_fondo)


def graficar():
    """
    Function to plot a graph based on the provided formula and range.

    This function first plays a sound, then checks if the formula input is empty.
    If the formula is empty, it displays an error message.
    Otherwise, it plots the graph using the formula, range, and a specified frame.

    Parameters:
    - None

    Returns:
    - None
    """
    reproducirSonido()
    if txt_formula.get() == "":
        messagebox.showerror("Error", "No hay formula")
    else:
        grafico(txt_formula, txt_rango, txt_rango1, frame2)


def limpiar():
    """
    Clears the input fields, the treeview, and updates the graph.
    """
    reproducirSonido()
    txt_formula.delete(0, END)
    txt_intervaloA.delete(0, END)
    txt_intervaloB.delete(0, END)
    trv.delete(*trv.get_children())
    eGrafico()
    eL()


def teclado():
    """
    This function toggles the keyboard display on the GUI.

    If the keyboard is currently hidden, it will be displayed by calling the cKeyboard function.
    If the keyboard is currently displayed, it will be hidden by calling the dKeyboard function.
    The global variable 'bandera' is used to keep track of the current state of the keyboard.

    Parameters:
    None

    Returns:
    None
    """
    global bandera
    if bandera == False:
        cKeyboard(
            root,
            click_boton,
            img_sin,
            img_cos,
            img_tg,
            img_ln,
            img_log,
            img_raiz,
            img_exp,
            img_elevado,
            img_pi,
            img_parentesis_izq,
            img_parentesis_der,
            img_suma,
            img_resta,
            img_multiplicacion,
            img_division,
        )
        bandera = True
    else:
        dKeyboard()
        bandera = False


if __name__ == "__main__":
    root = customtkinter.CTk()
    pygame.init()
    pygame.mixer.init()
    frame = customtkinter.CTkFrame(master=root, width=1280, height=720)
    frame.place(x=0, y=0)

    frame2 = customtkinter.CTkFrame(
        master=root, width=640, height=720, bg_color="#ffffff"
    )
    frame2.place(x=640, y=100)
    txt_rango = customtkinter.CTkEntry(
        master=frame, font=("Roboto", 15), width=140, justify="center"
    )
    txt_rango.place(x=280, y=240)
    txt_rango.insert(END, "-20,20")
    txt_rango1 = customtkinter.CTkEntry(
        master=frame, font=("Roboto", 15), width=140, justify="center"
    )
    txt_rango1.place(x=450, y=240)
    txt_rango1.insert(END, "-20,20")
    txt_formula = customtkinter.CTkEntry(
        master=frame,
        font=("Roboto", 15),
        width=180,
        justify="center",
        placeholder_text="Ej: sin(x)",
        border_width=2,
    )
    txt_formula.place(x=340, y=170)
    txt_intervaloA = customtkinter.CTkEntry(
        master=frame,
        font=("Roboto", 15),
        width=140,
        justify="center",
        placeholder_text="Ej: -1 o 0",
        border_width=2,
    )
    txt_intervaloA.place(x=280, y=320)
    txt_intervaloB = customtkinter.CTkEntry(
        master=frame,
        font=("Roboto", 15),
        width=140,
        justify="center",
        placeholder_text="Ej: 0 o 1",
        border_width=2,
    )
    txt_intervaloB.place(x=450, y=320)
    textoAutores = customtkinter.CTkLabel(
        master=frame,
        text="Desarrollado por: Gorotiza - García - Masache",
        font=("Roboto", 16),
    )
    textoAutores.place(x=155, y=670)

    img1 = customtkinter.CTkImage(
        light_image=Image.open("Recursos/calculadora1.png"),
        dark_image=Image.open("Recursos/calculadora.png"),
        size=(36, 36),
    )
    img2 = customtkinter.CTkImage(
        light_image=Image.open("Recursos/grafica1.png"),
        dark_image=Image.open("Recursos/grafica.png"),
        size=(36, 36),
    )
    img3 = customtkinter.CTkImage(
        light_image=Image.open("Recursos/limpiar1.png"),
        dark_image=Image.open("Recursos/limpiar.png"),
        size=(36, 36),
    )
    img4 = customtkinter.CTkImage(
        light_image=Image.open("Recursos/info1.png"),
        dark_image=Image.open("Recursos/info.png"),
        size=(24, 24),
    )
    img5 = customtkinter.CTkImage(
        light_image=Image.open("Recursos/tema1.png"),
        dark_image=Image.open("Recursos/tema.png"),
        size=(24, 24),
    )
    img6 = customtkinter.CTkImage(
        light_image=Image.open("Recursos/help1.png"),
        dark_image=Image.open("Recursos/help.png"),
        size=(36, 36),
    )
    img7 = customtkinter.CTkImage(
        light_image=Image.open("Recursos/teclado1.png"),
        dark_image=Image.open("Recursos/teclado.png"),
        size=(24, 24),
    )

    img_sin = customtkinter.CTkImage(
        light_image=Image.open("Recursos/sin1.png"),
        dark_image=Image.open("Recursos/sin.png"),
        size=(24, 24),
    )
    img_cos = customtkinter.CTkImage(
        light_image=Image.open("Recursos/cos1.png"),
        dark_image=Image.open("Recursos/cos.png"),
        size=(24, 24),
    )
    img_tg = customtkinter.CTkImage(
        light_image=Image.open("Recursos/tan1.png"),
        dark_image=Image.open("Recursos/tan.png"),
        size=(24, 24),
    )
    img_ln = customtkinter.CTkImage(
        light_image=Image.open("Recursos/ln1.png"),
        dark_image=Image.open("Recursos/ln.png"),
        size=(24, 24),
    )
    img_log = customtkinter.CTkImage(
        light_image=Image.open("Recursos/log1.png"),
        dark_image=Image.open("Recursos/log.png"),
        size=(24, 24),
    )
    img_raiz = customtkinter.CTkImage(
        light_image=Image.open("Recursos/raiz1.png"),
        dark_image=Image.open("Recursos/raiz.png"),
        size=(24, 24),
    )
    img_exp = customtkinter.CTkImage(
        light_image=Image.open("Recursos/exp1.png"),
        dark_image=Image.open("Recursos/exp.png"),
        size=(24, 24),
    )
    img_elevado = customtkinter.CTkImage(
        light_image=Image.open("Recursos/elevado1.png"),
        dark_image=Image.open("Recursos/elevado.png"),
        size=(24, 24),
    )
    img_pi = customtkinter.CTkImage(
        light_image=Image.open("Recursos/pi1.png"),
        dark_image=Image.open("Recursos/pi.png"),
        size=(24, 24),
    )
    img_parentesis_izq = customtkinter.CTkImage(
        light_image=Image.open("Recursos/parentesis_izq1.png"),
        dark_image=Image.open("Recursos/parentesis_izq.png"),
        size=(24, 24),
    )
    img_parentesis_der = customtkinter.CTkImage(
        light_image=Image.open("Recursos/parentesis_der1.png"),
        dark_image=Image.open("Recursos/parentesis_der.png"),
        size=(24, 24),
    )
    img_suma = customtkinter.CTkImage(
        light_image=Image.open("Recursos/suma1.png"),
        dark_image=Image.open("Recursos/suma.png"),
        size=(24, 24),
    )
    img_resta = customtkinter.CTkImage(
        light_image=Image.open("Recursos/resta1.png"),
        dark_image=Image.open("Recursos/resta.png"),
        size=(24, 24),
    )
    img_multiplicacion = customtkinter.CTkImage(
        light_image=Image.open("Recursos/multiplicacion1.png"),
        dark_image=Image.open("Recursos/multiplicacion.png"),
        size=(24, 24),
    )
    img_division = customtkinter.CTkImage(
        light_image=Image.open("Recursos/division1.png"),
        dark_image=Image.open("Recursos/division.png"),
        size=(24, 24),
    )

    lbl_img1 = customtkinter.CTkLabel(master=frame, image=img1, text="")
    lbl_img1.place(x=30, y=283)
    lbl_img2 = customtkinter.CTkLabel(master=frame, image=img2, text="")
    lbl_img2.place(x=30, y=223)
    lbl_img3 = customtkinter.CTkLabel(master=frame, image=img3, text="")
    lbl_img3.place(x=30, y=163)
    lbl_img4 = customtkinter.CTkLabel(master=frame, image=img4, text="")
    lbl_img4.place(x=600, y=210)
    lbl_img5 = customtkinter.CTkLabel(master=frame, image=img5, text="")
    lbl_img5.place(x=960, y=19)

    Hovertip(
        lbl_img4,
        text="¿Qué valor ingresar?\nLim X\nRepresentará el eje de las abscisas.\nPor ejemplo: -20,20\n\nLim Y\nRepresentará el eje de las ordenadas.\nPor ejemplo: -20,20",
        hover_delay=500,
    )

    lbl_titulo = customtkinter.CTkLabel(
        master=frame, text="Métodos Numéricos", font=("Roboto", 25)
    )
    lbl_titulo.place(x=530, y=15)
    lbl_formula = customtkinter.CTkLabel(
        master=frame, text="Ingrese Fórmula", font=("Roboto", 20)
    )
    lbl_formula.place(x=360, y=130)
    lbl_intervaloA = customtkinter.CTkLabel(
        master=frame, text="Ingrese Intervalo [Xa]", font=("Roboto", 15)
    )
    lbl_intervaloA.place(x=280, y=280)
    lbl_intervaloB = customtkinter.CTkLabel(
        master=frame, text="Ingrese Intervalo [Xb]", font=("Roboto", 15)
    )
    lbl_intervaloB.place(x=450, y=280)
    lbl_table = customtkinter.CTkLabel(
        master=frame, text="Tabla de Resultados", font=("Roboto", 24)
    )
    lbl_table.place(x=230, y=370)
    lbl_grafica = customtkinter.CTkLabel(
        master=frame2, text="Gráfica", font=("Roboto", 24)
    )
    lbl_grafica.pack(pady=10)
    lbl_rango = customtkinter.CTkLabel(master=frame, text="Lim X", font=("Roboto", 20))
    lbl_rango.place(x=330, y=210)
    lbl_rango1 = customtkinter.CTkLabel(master=frame, text="Lim Y", font=("Roboto", 20))
    lbl_rango1.place(x=490, y=210)
    lbl_combo = customtkinter.CTkLabel(
        master=frame, text="Seleccione un Método:", font=("Roboto", 14)
    )
    lbl_combo.place(x=10, y=60)

    style = ttk.Style()

    style.theme_use("alt")
    style.configure(
        "Treeview.Heading",
        background="#424141",
        foreground="white",
        fieldbackground="black",
    )
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

    btn_calcular = customtkinter.CTkButton(
        master=frame,
        text="Calcular",
        width=150,
        height=40,
        font=("Roboto", 16),
        command=Metodos.accionesARealizar,
        border_width=2,
    )
    btn_calcular.place(x=80, y=280)
    btn_graficar = customtkinter.CTkButton(
        master=frame,
        text="Graficar",
        width=150,
        height=40,
        font=("Roboto", 16),
        command=graficar,
        border_width=2,
    )
    btn_graficar.place(x=80, y=220)
    btn_limpiar = customtkinter.CTkButton(
        master=frame,
        text="Nuevo",
        width=150,
        height=40,
        font=("Roboto", 16),
        command=limpiar,
        border_width=2,
    )
    btn_limpiar.place(x=80, y=160)
    btn_usuario = customtkinter.CTkButton(
        master=frame,
        image=img6,
        text="",
        command=Metodos.abrirManual,
        width=36,
        height=36,
    )
    btn_usuario.place(x=30, y=655)
    # btn_calculadora = toggle(root,  dKeyboard)
    btn_calculadora = customtkinter.CTkButton(
        master=frame, text="", image=img7, width=24, height=24, command=teclado
    )
    btn_calculadora.place(x=540, y=167)

    cmb_modo = customtkinter.CTkOptionMenu(
        master=frame,
        values=[
            "System",
            "Dark",
            "Light",
        ],
        width=220,
        command=Metodos.change_appearance_mode_event,
    )
    cmb_modo.place(x=1000, y=20)

    cmb_metodos = customtkinter.CTkComboBox(
        master=frame,
        values=["", "Método de Bisección", "Método de Falsa Posición"],
        width=220,
    )
    cmb_metodos.place(x=170, y=60)

    Metodos = Metodos(root)

root.mainloop()
