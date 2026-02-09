"""
Formulario Presupuesto - Cesión de Derechos Onerosa.
"""
import tkinter as tk
from tkinter import messagebox

import config
import datos
import formatos
from ui.base_presupuesto import BasePresupuestoWindow
from impresion import dibujar_cesion


class CesiondWindow(BasePresupuestoWindow):
    TIPO_OPERACION = "Cesión de derechos onerosa"
    TIENE_REPOSICION = True
    USA_GEN_HTML = "gen"

    def _calcular(self):
        try:
            ve = formatos.parse_decimal(self.veconomico.get())
        except ValueError:
            messagebox.showerror("Error", "El Valor económico debe ser numérico")
            return
        if self._validar_otros():
            return
        d = config.get_presupuesto_defaults()
        ve_str = datos.agrega_decimales(str(ve))
        self.veconomico.delete(0, tk.END)
        self.veconomico.insert(0, ve_str)
        arancel = ve * d["tasa_arancel"] + d["arancel_fijo"]
        self._set_entry("arancel", datos.agrega_decimales(str(arancel)))
        self._set_entry("certificado", formatos.formatear_decimal(d["certificado_base"]))
        self._set_entry("aportes1", datos.agrega_decimales(str((arancel / 2) * 0.18)))
        self._set_entry("aportes2", datos.agrega_decimales(str(ve * d["aportes2_porcentaje"])))
        repos = max(ve * d["reposicion_porcentaje"], d["reposicion_minimo"])
        self._set_entry("reposicion", datos.agrega_decimales(str(repos)))
        anot = max(ve * d["anotacion_porcentaje"], d["anotacion_minimo"])
        self._set_entry("anotacion", datos.agrega_decimales(str(anot)))
        self._set_entry("goperativo", formatos.formatear_decimal(d["goperativo"]))
        self._set_entry("protoley", formatos.formatear_decimal(d["protoley"]))
        self._set_entry("total", self._sumar_todo())
        self._habilitar_campos()

    def _validar_otros(self) -> bool:
        for i in (1, 2, 3):
            try:
                formatos.parse_decimal(self.entries[f"otros{i}"].get())
            except ValueError:
                messagebox.showerror(
                    "Error",
                    f"{self.entries[f'notros{i}'].get()} debe ser numérico"
                )
                return True
        return False

    def _get_html(self) -> str:
        esc = config.get_escribania()
        return datos.gen_html(
            "Escribanía " + esc["nombre"],
            esc["direccion"],
            esc["telefono"],
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
            "Escritura de Cesión de Derechos Onerosa",
        )

    def _imprimir(self):
        dibujar_cesion(
            self.arancel.get(), self.certificado.get(),
            self.aportes1.get(), self.aportes2.get(),
            self.reposicion.get(), self.anotacion.get(),
            self.goperativo.get(), self.protoley.get(),
            self.otros1.get(), self.otros2.get(), self.otros3.get(),
            self.notros1.get(), self.notros2.get(), self.notros3.get(),
            self.total.get(), self.partes.get(), self.veconomico.get(),
            self.btn_bajar.cget("bg") == "red",
        )
