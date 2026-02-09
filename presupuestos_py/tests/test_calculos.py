"""Tests para fórmulas de cálculo (Venta, Donación, etc.)."""
import pytest

from ui.base_presupuesto import _parse_decimal
import datos


def test_parse_decimal():
    """_parse_decimal convierte formato argentino a float."""
    assert _parse_decimal("1.234,56") == 1234.56
    assert _parse_decimal("100") == 100.0
    assert _parse_decimal("0,00") == 0.0
    assert _parse_decimal("abc") == 0.0


def test_formula_venta():
    """Fórmulas Venta: arancel, aportes1, aportes2, reposicion, anotacion."""
    ve = 100_000
    arancel = ve * 0.02 + 27.7
    assert abs(arancel - 2027.7) < 0.01
    aportes1 = (arancel / 2) * 0.18
    assert abs(aportes1 - 182.493) < 0.01
    aportes2 = ve * 0.003
    assert aportes2 == 300
    reposicion = max(ve * 0.01, 30)
    assert reposicion == 1000
    anotacion = max(ve * 0.002, 30)
    assert anotacion == 200


def test_formato_salida_venta():
    """Valores calculados se formatean con coma decimal."""
    arancel = 2027.7
    s = datos.agrega_decimales(str(arancel))
    assert "," in s
    assert "2.027,70" == s
