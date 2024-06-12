from math import *
from tkinter import *
from idlelib.tooltip import Hovertip
from PIL import Image
import customtkinter

def createTeclado(
    root: customtkinter.CTk,
    click_boton,
    img_sin: Image,
    img_cos: Image,
    img_tg: Image,
    img_ln: Image,
    img_log: Image,
    img_raiz: Image,
    img_exp: Image,
    img_elevado: Image,
    img_pi: Image,
    img_parentesis_izq: Image,
    img_parentesis_der: Image,
    img_suma: Image,
    img_resta: Image,
    img_multiplicacion: Image,
    img_division: Image,
):
    """
    Creates a custom keyboard interface for a calculator.

    Args:
        root (customtkinter.CTk): The root window of the calculator.
        click_boton (function): The function to be called when a button is clicked.
        img_sin (Image): The image for the sin button.
        img_cos (Image): The image for the cos button.
        img_tg (Image): The image for the tg button.
        img_ln (Image): The image for the ln button.
        img_log (Image): The image for the log button.
        img_raiz (Image): The image for the square root button.
        img_exp (Image): The image for the exponential button.
        img_elevado (Image): The image for the power button.
        img_pi (Image): The image for the pi button.
        img_parentesis_izq (Image): The image for the left parenthesis button.
        img_parentesis_der (Image): The image for the right parenthesis button.
        img_suma (Image): The image for the addition button.
        img_resta (Image): The image for the subtraction button.
        img_multiplicacion (Image): The image for the multiplication button.
        img_division (Image): The image for the division button.
    """
    global frameCalc
    frameCalc = Frame(root, width=260, height=130, background="#cbc1a9")
    frameCalc.place(x=295, y=220)
    btn_sen = customtkinter.CTkButton(
        master=frameCalc,
        text="",
        width=24,
        height=24,
        image=img_sin,
        command=lambda: click_boton("sin()"),
    )
    btn_sen.place(x=10, y=10)

    btn_cos = customtkinter.CTkButton(
        master=frameCalc,
        text="",
        width=24,
        height=24,
        image=img_cos,
        command=lambda: click_boton("cos()"),
    )
    btn_cos.place(x=60, y=10)

    btn_tg = customtkinter.CTkButton(
        master=frameCalc,
        text="",
        width=24,
        height=24,
        image=img_tg,
        command=lambda: click_boton("tan()"),
    )
    btn_tg.place(x=110, y=10)

    btn_ln = customtkinter.CTkButton(
        master=frameCalc,
        text="",
        width=24,
        height=24,
        image=img_ln,
        command=lambda: click_boton("ln()"),
    )
    btn_ln.place(x=160, y=10)

    btn_log = customtkinter.CTkButton(
        master=frameCalc,
        text="",
        width=24,
        height=24,
        image=img_log,
        command=lambda: click_boton("log()"),
    )
    btn_log.place(x=210, y=10)

    btn_raiz = customtkinter.CTkButton(
        master=frameCalc,
        text="",
        width=24,
        height=24,
        image=img_raiz,
        command=lambda: click_boton("sqrt()"),
    )
    btn_raiz.place(x=10, y=50)

    btn_exp = customtkinter.CTkButton(
        master=frameCalc,
        text="",
        width=24,
        height=24,
        image=img_exp,
        command=lambda: click_boton("exp()"),
    )
    btn_exp.place(x=60, y=50)

    btn_elevado = customtkinter.CTkButton(
        master=frameCalc,
        text="",
        width=24,
        height=24,
        image=img_elevado,
        command=lambda: click_boton("^"),
    )
    btn_elevado.place(x=110, y=50)

    btn_pi = customtkinter.CTkButton(
        master=frameCalc,
        text="",
        width=24,
        height=24,
        image=img_pi,
        command=lambda: click_boton("pi"),
    )
    btn_pi.place(x=160, y=50)

    btn_parentesis_izq = customtkinter.CTkButton(
        master=frameCalc,
        text="",
        width=24,
        height=24,
        image=img_parentesis_izq,
        command=lambda: click_boton("("),
    )
    btn_parentesis_izq.place(x=210, y=50)

    btn_parentesis_der = customtkinter.CTkButton(
        master=frameCalc,
        text="",
        width=24,
        height=24,
        image=img_parentesis_der,
        command=lambda: click_boton(")"),
    )
    btn_parentesis_der.place(x=10, y=90)

    btn_suma = customtkinter.CTkButton(
        master=frameCalc,
        text="",
        width=24,
        height=24,
        image=img_suma,
        command=lambda: click_boton("+"),
    )
    btn_suma.place(x=60, y=90)

    btn_resta = customtkinter.CTkButton(
        master=frameCalc,
        text="",
        width=24,
        height=24,
        image=img_resta,
        command=lambda: click_boton("-"),
    )
    btn_resta.place(x=110, y=90)

    btn_multiplicacion = customtkinter.CTkButton(
        master=frameCalc,
        text="",
        width=24,
        height=24,
        image=img_multiplicacion,
        command=lambda: click_boton("*"),
    )
    btn_multiplicacion.place(x=160, y=90)

    btn_division = customtkinter.CTkButton(
        master=frameCalc,
        text="",
        width=24,
        height=24,
        image=img_division,
        command=lambda: click_boton("/"),
    )
    btn_division.place(x=210, y=90)


def deleteTeclado():
    """
    Deletes the teclado frame.
    """
    frameCalc.destroy()
