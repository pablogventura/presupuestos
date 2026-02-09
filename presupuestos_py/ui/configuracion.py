"""
Diálogo de configuración.
"""
import tkinter as tk
from tkinter import ttk

import config


class ConfiguracionDialog:
    def __init__(self, parent):
        self.win = tk.Toplevel(parent)
        self.win.title("Configuración de Presupuestos")
        self.win.resizable(False, False)
        self.win.transient(parent)
        self.win.grab_set()

        # Escribanía
        frame_esc = ttk.LabelFrame(self.win, text="Escribanía:", padding=10)
        frame_esc.pack(fill=tk.X, padx=10, pady=5)

        ttk.Label(frame_esc, text="Nombre:").grid(row=0, column=0, sticky=tk.W, pady=2)
        self.nombre = ttk.Entry(frame_esc, width=35)
        self.nombre.grid(row=0, column=1, sticky=tk.EW, pady=2, padx=(5, 0))

        ttk.Label(frame_esc, text="Dirección:").grid(row=1, column=0, sticky=tk.W, pady=2)
        self.direccion = ttk.Entry(frame_esc, width=35)
        self.direccion.grid(row=1, column=1, sticky=tk.EW, pady=2, padx=(5, 0))

        ttk.Label(frame_esc, text="Teléfono - E-mail:").grid(
            row=2, column=0, sticky=tk.W, pady=2
        )
        self.telefono = ttk.Entry(frame_esc, width=35)
        self.telefono.grid(row=2, column=1, sticky=tk.EW, pady=2, padx=(5, 0))

        # Impresión
        frame_imp = ttk.LabelFrame(self.win, text="Impresión:", padding=10)
        frame_imp.pack(fill=tk.X, padx=10, pady=5)

        ttk.Label(frame_imp, text="Margen superior (twips):").grid(
            row=0, column=0, sticky=tk.W, pady=2
        )
        self.margen = ttk.Entry(frame_imp, width=15)
        self.margen.grid(row=0, column=1, sticky=tk.W, pady=2, padx=(5, 0))

        # Botones
        frame_btn = ttk.Frame(self.win, padding=10)
        frame_btn.pack(fill=tk.X)

        ttk.Button(frame_btn, text="Aceptar", command=self._aceptar).pack(
            side=tk.RIGHT, padx=5
        )
        ttk.Button(frame_btn, text="Cancelar", command=self.win.destroy).pack(
            side=tk.RIGHT
        )

        self._cargar()
        self.win.wait_window()

    def _cargar(self):
        self.nombre.insert(0, config.get("Escribania", "Nombre", "Ventura"))
        self.direccion.insert(
            0,
            config.get(
                "Escribania",
                "Direccion",
                'Corrientes 5 - 4º "A"',
            ),
        )
        self.telefono.insert(
            0,
            config.get(
                "Escribania",
                "Telefonoemail",
                "Te: 4255715 - e-mail: gabventura@arnet.com.ar",
            ),
        )
        self.margen.insert(0, config.get("Impresion", "MargenSuperior", "4000"))

    def _aceptar(self):
        config.set_value("Escribania", "Nombre", self.nombre.get())
        config.set_value("Escribania", "Direccion", self.direccion.get())
        config.set_value("Escribania", "Telefonoemail", self.telefono.get())
        config.set_value("Impresion", "MargenSuperior", self.margen.get())
        self.win.destroy()
