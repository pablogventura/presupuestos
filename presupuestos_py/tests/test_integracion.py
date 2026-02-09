"""Tests de integración: flujos completos."""
import os
import tempfile

import pytest

import datos


def test_flujo_calcular_exportar_html_venta():
    """Flujo: Calcular Venta → Exportar HTML → verificar contenido."""
    # Simula datos de una Venta calculada
    html = datos.gen_html(
        "Escribanía Test",
        "Calle 1",
        "Tel 123",
        "Vendedor y Comprador",
        "100.000,00",
        "2.027,70",
        "700,00",
        "182,49",
        "300,00",
        "1.000,00",
        "200,00",
        "1.000,00",
        "4.410,19",
        "Otros:",
        "0,00",
        "Otros:",
        "0,00",
        "Otros:",
        "0,00",
        "Escritura de Venta",
    )
    assert "<html>" in html
    assert "100.000,00" in html
    assert "4.410,19" in html
    assert "Escritura de Venta" in html


def test_flujo_generar_pdf_guarda_archivo():
    """Flujo: Generar PDF → verificar que existe y tiene tamaño > 0."""
    pytest.importorskip("reportlab")
    from impresion import _generar_pdf

    with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as f:
        ruta = f.name
    try:
        _generar_pdf(
            "Test",
            "",
            "100.000,00", "2.027,70", "700,00", "182,49", "300,00", "30,00",
            "1.000,00", "150,00",
            "0,00", "0,00", "0,00",
            "Otros:", "Otros:", "Otros:",
            "4.420,19",
            False,
            False,
            ruta_destino=ruta,
        )
        assert os.path.exists(ruta)
        assert os.path.getsize(ruta) > 100
    finally:
        if os.path.exists(ruta):
            os.unlink(ruta)
