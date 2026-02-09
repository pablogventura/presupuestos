"""
Formulario Presupuesto - Donación.
"""
import tkinter as tk

import config
import datos
import formatos
from ui.base_presupuesto import BasePresupuestoWindow
from impresion import dibujar_donacion


class DonacionWindow(BasePresupuestoWindow):
    TIPO_OPERACION = "Donación"
    TIENE_REPOSICION = False
    USA_GEN_HTML = "gen_donacion"

    def _calcular(self):
        ve = formatos.parse_decimal(self.veconomico.get())
        if self._validar_otros():
            return
        self._aplicar_calculo(ve)

    def _get_html(self) -> str:
        esc = config.get_escribania()
        return datos.gen_html_donacion(
            "Escribanía " + esc["nombre"],
            esc["direccion"],
            esc["telefono"],
            self.partes.get(),
            self.veconomico.get(),
            self.arancel.get(),
            self.certificado.get(),
            self.aportes1.get(),
            self.aportes2.get(),
            self.anotacion.get(),
            self.goperativo.get(),
            self.total.get(),
            self.notros1.get(),
            self.otros1.get(),
            self.notros2.get(),
            self.otros2.get(),
            self.notros3.get(),
            self.otros3.get(),
        )

    def _imprimir(self):
        self._formatear_todos_los_numeros()
        dibujar_donacion(
            self.arancel.get(), self.certificado.get(),
            self.aportes1.get(), self.aportes2.get(),
            self.anotacion.get(), self.goperativo.get(),
            self.protoley.get(),
            self.otros1.get(), self.otros2.get(), self.otros3.get(),
            self.notros1.get(), self.notros2.get(), self.notros3.get(),
            self.total.get(), self.partes.get(), self.veconomico.get(),
            self.btn_bajar.cget("bg") == "red",
        )

    def _imprimir_a_archivo(self, path: str) -> None:
        dibujar_donacion(
            self.arancel.get(), self.certificado.get(),
            self.aportes1.get(), self.aportes2.get(),
            self.anotacion.get(), self.goperativo.get(),
            self.protoley.get(),
            self.otros1.get(), self.otros2.get(), self.otros3.get(),
            self.notros1.get(), self.notros2.get(), self.notros3.get(),
            self.total.get(), self.partes.get(), self.veconomico.get(),
            self.btn_bajar.cget("bg") == "red",
            ruta_destino=path,
        )
