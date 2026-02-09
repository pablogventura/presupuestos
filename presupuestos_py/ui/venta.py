"""
Formulario Presupuesto - Escritura de Venta.
"""
import tkinter as tk
from tkinter import messagebox

import config
import datos
from ui.base_presupuesto import BasePresupuestoWindow, _parse_decimal
from impresion import dibujar_venta


class VentaWindow(BasePresupuestoWindow):
    TIPO_OPERACION = "Venta"
    TIENE_REPOSICION = True
    USA_GEN_HTML = "gen"

    def _calcular(self):
        try:
            ve = _parse_decimal(self.veconomico.get())
        except ValueError:
            messagebox.showerror("Error", "El Valor económico debe ser numérico")
            return
        if self._validar_otros():
            return
        ve_str = datos.agrega_decimales(str(ve))
        self.veconomico.delete(0, tk.END)
        self.veconomico.insert(0, ve_str)
        arancel = ve * 0.02 + 27.7
        self._set_entry("arancel", datos.agrega_decimales(str(arancel)))
        self._set_entry("certificado", "700,00")
        self._set_entry("aportes1", datos.agrega_decimales(str((arancel / 2) * 0.18)))
        self._set_entry("aportes2", datos.agrega_decimales(str(ve * 0.003)))
        repos = max(ve * 0.01, 30)
        self._set_entry("reposicion", datos.agrega_decimales(str(repos)))
        anot = max(ve * 0.002, 30)
        self._set_entry("anotacion", datos.agrega_decimales(str(anot)))
        self._set_entry("goperativo", "1.000,00")
        self._set_entry("protoley", "150,00")
        self._set_entry("total", self._sumar_todo())
        self._habilitar_campos()

    def _validar_otros(self) -> bool:
        for i in (1, 2, 3):
            try:
                _parse_decimal(self.entries[f"otros{i}"].get())
            except ValueError:
                messagebox.showerror(
                    "Error",
                    f"{self.entries[f'notros{i}'].get()} debe ser numérico"
                )
                return True
        return False

    def _get_html(self) -> str:
        esc = "Escribanía " + config.get("Escribania", "Nombre", "Ventura")
        return datos.gen_html(
            esc,
            config.get("Escribania", "Direccion", 'Corrientes 5 - 4º "A"'),
            config.get("Escribania", "Telefonoemail", "Te: 4255715 - e-mail: gabventura@arnet.com.ar"),
            self.partes.get(),
            self.veconomico.get(),
            self.arancel.get(),
            self.certificado.get(),
            self.aportes1.get(),
            self.aportes2.get(),
            self.reposicion.get(),
            self.anotacion.get(),
            self.goperativo.get(),
            self.total.get(),
            self.notros1.get(),
            self.otros1.get(),
            self.notros2.get(),
            self.otros2.get(),
            self.notros3.get(),
            self.otros3.get(),
            "Escritura de Venta",
        )

    def _imprimir(self):
        dibujar_venta(
            self.arancel.get(), self.certificado.get(),
            self.aportes1.get(), self.aportes2.get(),
            self.reposicion.get(), self.anotacion.get(),
            self.goperativo.get(), self.protoley.get(),
            self.otros1.get(), self.otros2.get(), self.otros3.get(),
            self.notros1.get(), self.notros2.get(), self.notros3.get(),
            self.total.get(), self.partes.get(), self.veconomico.get(),
            self.btn_bajar.cget("bg") == "red",
        )
