"""
Ventana principal - menú de operaciones.
"""
import tkinter as tk
from tkinter import ttk, messagebox

from ui.configuracion import ConfiguracionDialog
from utils import centrar_ventana
from ui.venta import VentaWindow
from ui.donacion import DonacionWindow
from ui.cesiond import CesiondWindow
from ui.particion import ParticionWindow


class PrincipalWindow:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.win = tk.Toplevel(root)
        self.win.title("Presupuestos")
        self.win.resizable(False, False)
        self.win.protocol("WM_DELETE_WINDOW", self._on_close)

        frame_op = ttk.LabelFrame(self.win, text="Operación:", padding=10)
        frame_op.pack(fill=tk.X, padx=10, pady=10)

        self.cbo = ttk.Combobox(frame_op, state="readonly", width=30)
        self.cbo["values"] = (
            "Donación",
            "Venta",
            "Cesión de derechos onerosa",
            "Partición o Adjudicación",
        )
        self.cbo.pack(fill=tk.X, pady=5)
        self.cbo.current(0)
        self.cbo.bind("<<ComboboxSelected>>", self._on_operacion)

        frame_btn = ttk.Frame(self.win, padding=10)
        frame_btn.pack(fill=tk.X)

        ttk.Button(frame_btn, text="Configuración", command=self._on_config).pack(
            side=tk.LEFT, padx=(0, 5)
        )
        ttk.Button(frame_btn, text="Salir", command=self._on_salir).pack(side=tk.LEFT)

        self._op_window = None
        centrar_ventana(self.win)

    def _on_operacion(self, event=None):
        op = self.cbo.get()
        self.win.withdraw()
        if op == "Venta":
            self._op_window = VentaWindow(self.root, self._on_volver)
        elif op == "Donación":
            self._op_window = DonacionWindow(self.root, self._on_volver)
        elif op == "Cesión de derechos onerosa":
            self._op_window = CesiondWindow(self.root, self._on_volver)
        elif op == "Partición o Adjudicación":
            self._op_window = ParticionWindow(self.root, self._on_volver)
        if self._op_window:
            self._op_window.show()

    def _on_volver(self):
        if self._op_window:
            self._op_window = None
        self.win.deiconify()

    def _on_config(self):
        ConfiguracionDialog(self.win)

    def _on_salir(self):
        self.root.quit()

    def _on_close(self):
        self.root.quit()

    def show(self):
        self.win.deiconify()
        self.win.lift()
        self.win.focus_force()
