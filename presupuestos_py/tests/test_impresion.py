"""Tests para el módulo impresion."""
import os

import pytest

pytest.importorskip("reportlab")
def test_generar_pdf_crea_archivo():
    """_generar_pdf crea un archivo PDF válido."""
    from impresion import _generar_pdf

    ruta = _generar_pdf(
        "Test Presupuesto",
        "Partes del contrato",
        "100.000,00",
        "2.027,70",
        "700,00",
        "182,49",
        "300,00",
        "30,00",
        "1.000,00",
        "150,00",
        "0,00",
        "0,00",
        "0,00",
        "Otros:",
        "Otros:",
        "Otros:",
        "4.420,19",
        False,
        False,
    )
    assert os.path.exists(ruta)
    assert ruta.endswith(".pdf")
    assert os.path.getsize(ruta) > 100
    os.unlink(ruta)
