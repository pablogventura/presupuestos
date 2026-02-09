"""
Diálogo de configuración.
"""
import tkinter as tk
from tkinter import ttk, messagebox

import config
from utils import centrar_ventana


def _twips_a_unidad(twips: float, unidad: str) -> float:
    """Convierte twips a mm, pt o twips."""
    if unidad == "mm":
        return twips * 25.4 / 1440
    if unidad == "pt":
        return twips / 20
    return twips


def _unidad_a_twips(valor: float, unidad: str) -> int:
    """Convierte valor en mm, pt o twips a twips."""
    if unidad == "mm":
        return int(valor * 1440 / 25.4)
    if unidad == "pt":
        return int(valor * 20)
    return int(valor)


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

        ttk.Label(frame_imp, text="Margen superior:").grid(
            row=0, column=0, sticky=tk.W, pady=2
        )
        self.margen = ttk.Entry(frame_imp, width=10)
        self.margen.grid(row=0, column=1, sticky=tk.W, pady=2, padx=(5, 0))
        self.margen_unidad = ttk.Combobox(
            frame_imp, width=8, values=["mm", "pt", "twips"], state="readonly"
        )
        self.margen_unidad.grid(row=0, column=2, sticky=tk.W, padx=(5, 0))

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
        centrar_ventana(self.win)
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
        twips = int(config.get("Impresion", "MargenSuperior", "4000"))
        unidad = config.get("Impresion", "MargenUnidad", "twips")
        self.margen_unidad.set(unidad if unidad in ("mm", "pt", "twips") else "twips")
        val_display = _twips_a_unidad(twips, self.margen_unidad.get())
        self.margen.insert(0, str(round(val_display, 2) if val_display != int(val_display) else int(val_display)))

    def _aceptar(self):
        margen_val = self.margen.get().strip()
        if not margen_val:
            messagebox.showerror("Error", "El margen superior no puede estar vacío.")
            return
        try:
            t = margen_val.replace(".", "").replace(",", ".")
            v = float(t)
        except ValueError:
            messagebox.showerror(
                "Error",
                "El margen superior debe ser un número válido (ej: 70 o 4.000).",
            )
            return
        if v < 0:
            messagebox.showerror("Error", "El margen superior debe ser un número positivo.")
            return
        twips = _unidad_a_twips(v, self.margen_unidad.get())
        config.set_value("Escribania", "Nombre", self.nombre.get())
        config.set_value("Escribania", "Direccion", self.direccion.get())
        config.set_value("Escribania", "Telefonoemail", self.telefono.get())
        config.set_value("Impresion", "MargenSuperior", str(twips))
        config.set_value("Impresion", "MargenUnidad", self.margen_unidad.get())
        self.win.destroy()
