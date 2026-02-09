"""Tests de UI/UX: ventanas, cálculos, validación y atajos."""
import tkinter as tk
from unittest.mock import patch

import pytest

pytest.importorskip("tkinter")


def _crear_ventana_venta():
    """Crea ventana de Venta con root oculto."""
    root = tk.Tk()
    root.withdraw()
    from ui.venta import VentaWindow

    ventana = None

    def on_volver():
        nonlocal ventana
        if ventana:
            ventana.win.destroy()
        root.destroy()

    ventana = VentaWindow(root, on_volver=on_volver)
    ventana.win.withdraw()
    return root, ventana, on_volver


@patch("ui.base_presupuesto.config.get_presupuesto_defaults")
@patch("ui.venta.config.get_escribania")
def test_calcular_llena_campos(mock_esc, mock_defaults):
    """Calcular con valor económico rellena arancel, certificado, total."""
    mock_defaults.return_value = {
        "certificado_base": 700,
        "goperativo": 1000,
        "protoley": 150,
        "tasa_arancel": 0.02,
        "arancel_fijo": 27.7,
        "reposicion_minimo": 30,
        "reposicion_porcentaje": 0.01,
        "anotacion_minimo": 30,
        "anotacion_porcentaje": 0.002,
        "aportes2_porcentaje": 0.003,
    }
    mock_esc.return_value = {"nombre": "Test", "direccion": "Dir", "telefono": "Tel"}

    root, ventana, on_volver = _crear_ventana_venta()
    try:
        ventana.veconomico.delete(0, tk.END)
        ventana.veconomico.insert(0, "100000")
        root.update_idletasks()

        ventana._calcular()
        root.update_idletasks()

        arancel = ventana.arancel.get()
        total = ventana.total.get()
        assert "2.027" in arancel or "2027" in arancel
        assert ventana.certificado.get() == "700,00"
        assert "," in total
        # Tras calcular, los campos están habilitados
        assert "disabled" not in str(ventana.arancel.cget("state"))
    finally:
        ventana.win.destroy()
        root.destroy()


@patch("ui.base_presupuesto.config.get_presupuesto_defaults")
@patch("ui.venta.config.get_escribania")
def test_validacion_valor_economico_invalido(mock_esc, mock_defaults):
    """Valor económico no numérico muestra mensaje de error en label."""
    mock_defaults.return_value = {
        "certificado_base": 700,
        "goperativo": 1000,
        "protoley": 150,
        "tasa_arancel": 0.02,
        "arancel_fijo": 27.7,
        "reposicion_minimo": 30,
        "reposicion_porcentaje": 0.01,
        "anotacion_minimo": 30,
        "anotacion_porcentaje": 0.002,
        "aportes2_porcentaje": 0.003,
    }
    mock_esc.return_value = {"nombre": "T", "direccion": "D", "telefono": "T"}

    root, ventana, _ = _crear_ventana_venta()
    try:
        ventana.veconomico.delete(0, tk.END)
        ventana.veconomico.insert(0, "abc")
        root.update_idletasks()

        ventana._on_ve_focusout()
        root.update_idletasks()

        assert ventana._lbl_ve_error.cget("text") == "Valor no numérico"
    finally:
        ventana.win.destroy()
        root.destroy()


@patch("ui.base_presupuesto.config.get_presupuesto_defaults")
@patch("ui.venta.config.get_escribania")
def test_validacion_valor_economico_valido_limpia_error(mock_esc, mock_defaults):
    """Valor económico válido no muestra error."""
    mock_defaults.return_value = {
        "certificado_base": 700,
        "goperativo": 1000,
        "protoley": 150,
        "tasa_arancel": 0.02,
        "arancel_fijo": 27.7,
        "reposicion_minimo": 30,
        "reposicion_porcentaje": 0.01,
        "anotacion_minimo": 30,
        "anotacion_porcentaje": 0.002,
        "aportes2_porcentaje": 0.003,
    }
    mock_esc.return_value = {"nombre": "T", "direccion": "D", "telefono": "T"}

    root, ventana, _ = _crear_ventana_venta()
    try:
        ventana.veconomico.delete(0, tk.END)
        ventana.veconomico.insert(0, "100000")
        root.update_idletasks()

        ventana._on_ve_focusout()
        root.update_idletasks()

        assert ventana._lbl_ve_error.cget("text") == ""
    finally:
        ventana.win.destroy()
        root.destroy()


@patch("ui.base_presupuesto.config.get_presupuesto_defaults")
@patch("ui.venta.config.get_escribania")
def test_actualizar_total_al_editar(mock_esc, mock_defaults):
    """Tras Calcular, editar un campo actualiza el Total."""
    mock_defaults.return_value = {
        "certificado_base": 700,
        "goperativo": 1000,
        "protoley": 150,
        "tasa_arancel": 0.02,
        "arancel_fijo": 27.7,
        "reposicion_minimo": 30,
        "reposicion_porcentaje": 0.01,
        "anotacion_minimo": 30,
        "anotacion_porcentaje": 0.002,
        "aportes2_porcentaje": 0.003,
    }
    mock_esc.return_value = {"nombre": "T", "direccion": "D", "telefono": "T"}

    root, ventana, _ = _crear_ventana_venta()
    try:
        ventana.veconomico.delete(0, tk.END)
        ventana.veconomico.insert(0, "100000")
        ventana._calcular()
        root.update_idletasks()

        total_antes = ventana.total.get()
        ventana.certificado.config(state="normal")
        ventana.certificado.delete(0, tk.END)
        ventana.certificado.insert(0, "0,00")
        ventana._actualizar_total()
        root.update_idletasks()

        total_despues = ventana.total.get()
        # _actualizar_total debe recalcular; al bajar certificado el total cambia
        assert "," in total_despues
        # Si el total se actualizó, debería ser menor (certificado 700->0)
        val_antes = float(total_antes.replace(".", "").replace(",", "."))
        val_despues = float(total_despues.replace(".", "").replace(",", "."))
        assert val_despues < val_antes
    finally:
        ventana.win.destroy()
        root.destroy()


@patch("ui.base_presupuesto.config.get_presupuesto_defaults")
@patch("ui.venta.config.get_escribania")
@patch("ui.base_presupuesto.filedialog.asksaveasfilename")
def test_atajo_ctrl_s_exportar_html(mock_asksave, mock_esc, mock_defaults):
    """Ctrl+S dispara exportar HTML."""
    mock_defaults.return_value = {
        "certificado_base": 700,
        "goperativo": 1000,
        "protoley": 150,
        "tasa_arancel": 0.02,
        "arancel_fijo": 27.7,
        "reposicion_minimo": 30,
        "reposicion_porcentaje": 0.01,
        "anotacion_minimo": 30,
        "anotacion_porcentaje": 0.002,
        "aportes2_porcentaje": 0.003,
    }
    mock_esc.return_value = {"nombre": "T", "direccion": "D", "telefono": "T"}
    mock_asksave.return_value = ""  # Cancelar diálogo

    root, ventana, _ = _crear_ventana_venta()
    try:
        ventana.veconomico.delete(0, tk.END)
        ventana.veconomico.insert(0, "100000")
        ventana._calcular()
        root.update_idletasks()

        event = type("Event", (), {"keysym": "s"})()
        result = ventana._on_ctrl_s(event)
        assert result == "break"
        mock_asksave.assert_called_once()
    finally:
        ventana.win.destroy()
        root.destroy()


@patch("ui.base_presupuesto.config.get_presupuesto_defaults")
@patch("ui.venta.config.get_escribania")
def test_atajo_ctrl_q_retorna_break(mock_esc, mock_defaults):
    """Ctrl+Q retorna break para evitar cierre por defecto."""
    mock_defaults.return_value = {
        "certificado_base": 700,
        "goperativo": 1000,
        "protoley": 150,
        "tasa_arancel": 0.02,
        "arancel_fijo": 27.7,
        "reposicion_minimo": 30,
        "reposicion_porcentaje": 0.01,
        "anotacion_minimo": 30,
        "anotacion_porcentaje": 0.002,
        "aportes2_porcentaje": 0.003,
    }
    mock_esc.return_value = {"nombre": "T", "direccion": "D", "telefono": "T"}

    root = tk.Tk()
    root.withdraw()
    from ui.venta import VentaWindow

    def on_volver():
        pass  # No destruir para poder hacer assertions

    ventana = VentaWindow(root, on_volver=on_volver)
    ventana.win.withdraw()
    try:
        event = type("Event", (), {"keysym": "q"})()
        result = ventana._on_ctrl_q(event)
        assert result == "break"
    finally:
        try:
            ventana.win.destroy()
            root.destroy()
        except tk.TclError:
            pass


@patch("ui.base_presupuesto.config.get_presupuesto_defaults")
@patch("ui.venta.config.get_escribania")
def test_calcular_base_devuelve_dict(mock_esc, mock_defaults):
    """_calcular_base devuelve dict con todos los valores."""
    mock_defaults.return_value = {
        "certificado_base": 700,
        "goperativo": 1000,
        "protoley": 150,
        "tasa_arancel": 0.02,
        "arancel_fijo": 27.7,
        "reposicion_minimo": 30,
        "reposicion_porcentaje": 0.01,
        "anotacion_minimo": 30,
        "anotacion_porcentaje": 0.002,
        "aportes2_porcentaje": 0.003,
    }
    mock_esc.return_value = {"nombre": "T", "direccion": "D", "telefono": "T"}

    root, ventana, _ = _crear_ventana_venta()
    try:
        vals = ventana._calcular_base(100_000)
        assert "arancel" in vals
        assert "certificado" in vals
        assert "aportes1" in vals
        assert "aportes2" in vals
        assert "reposicion" in vals
        assert "anotacion" in vals
        assert "goperativo" in vals
        assert "protoley" in vals
        assert "2.027" in vals["arancel"] or "2027" in vals["arancel"]
        assert vals["certificado"] == "700,00"
    finally:
        ventana.win.destroy()
        root.destroy()
