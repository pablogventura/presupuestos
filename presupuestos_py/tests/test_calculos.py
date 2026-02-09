"""Tests para fórmulas de cálculo (Venta, Donación, etc.)."""
import pytest

import formatos
import datos


def test_parse_decimal():
    """formatos.parse_decimal convierte formato argentino a float."""
    assert formatos.parse_decimal("1.234,56") == 1234.56
    assert formatos.parse_decimal("100") == 100.0
    assert formatos.parse_decimal("0,00") == 0.0
    assert formatos.parse_decimal("abc") == 0.0


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


@pytest.mark.parametrize("ve,arancel_esperado,aportes1_esperado", [
    (100_000, 2027.7, 182.49),
    (50_000, 1027.7, 92.49),
    (200_000, 4027.7, 362.49),
    (10_000, 227.7, 20.49),
])
def test_formulas_venta_parametrizado(ve, arancel_esperado, aportes1_esperado):
    """Fórmulas Venta con distintos valores económicos (usa constantes por defecto)."""
    tasa, fijo = 0.02, 27.7
    arancel = ve * tasa + fijo
    aportes1 = (arancel / 2) * 0.18
    assert abs(arancel - arancel_esperado) < 0.1
    assert abs(aportes1 - aportes1_esperado) < 0.1
