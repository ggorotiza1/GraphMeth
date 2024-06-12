import tkinter as tk
import customtkinter as ctk


class ToggleButton(ctk.CTkButton):
    """
    A custom toggle button widget.

    Inherits from ctk.CTkButton.

    Parameters:
    - parent: The parent widget.
    - command_on: The command to execute when the button is toggled on.
    - command_off: The command to execute when the button is toggled off.
    - **kwargs: Additional keyword arguments to pass to the parent widget.

    Attributes:
    - command_on: The command to execute when the button is toggled on.
    - command_off: The command to execute when the button is toggled off.
    - state: The current state of the button (True for on, False for off).

    Methods:
    - toggle: Toggles the state of the button and executes the corresponding command.

    Example usage:
    ```
    def on_button():
        print("Button toggled on")

    def off_button():
        print("Button toggled off")

    button = ToggleButton(parent, on_button, off_button, text="Toggle")
    button.pack()
    ```
    """

    def __init__(self, parent, command_on, command_off, **kwargs):
        super().__init__(parent, **kwargs)
        self.command_on = command_on
        self.command_off = command_off
        self.state = False
        self.configure(command=self.toggle)

    def toggle(self):
        """
        Toggles the state of the button and executes the corresponding command.

        If the button is currently off, it will be toggled on and the `command_on` will be executed.
        If the button is currently on, it will be toggled off and the `command_off` will be executed.
        """
        self.state = not self.state
        if self.state:
            self.configure(command=self.command_on)
            self.state = False
        else:
            self.configure(command=self.command_off)
            self.state = True
