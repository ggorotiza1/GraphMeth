import tkinter as tk
import customtkinter as ctk

class ToggleButton(ctk.CTkButton):
    def __init__(self, parent, command_on, command_off, **kwargs):
        # Inicializamos el botón
        super().__init__(parent, **kwargs)
        self.command_on = command_on
        self.command_off = command_off
        self.state = False
        self.configure(command=self.toggle)

    def toggle(self):
        self.state = not self.state
        if self.state:
            pass
            #self.configure(command=self.command_off)
            #self.state = False
        else:
            #self.configure(command=self.command_on)
            #self.state = True
            pass
