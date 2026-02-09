"""
Diálogo Acerca de.
"""
import tkinter as tk
from tkinter import ttk

from utils import VERSION


class AboutDialog:
    def __init__(self, parent):
        self.win = tk.Toplevel(parent)
        self.win.title("Acerca de Presupuestos")
        self.win.resizable(False, False)
        self.win.transient(parent)
        self.win.grab_set()

        frame = ttk.Frame(self.win, padding=20)
        frame.pack()

        ttk.Label(frame, text="Presupuestos", font=("", 14, "bold")).pack(anchor=tk.W)
        ttk.Label(frame, text=f"Versión {VERSION}").pack(anchor=tk.W)
        ttk.Label(frame, text="Contacto: pablogventura@gmail.com").pack(anchor=tk.W)
        ttk.Label(frame, text="© Pablo Ventura 2003-2011").pack(anchor=tk.W, pady=(10, 0))

        ttk.Button(frame, text="Aceptar", command=self.win.destroy).pack(pady=10)
        self.win.wait_window()
