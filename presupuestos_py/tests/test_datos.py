"""Tests para el módulo datos."""
import pytest
import datos


class TestAgregaDecimales:
    """Tests para datos.agrega_decimales."""

    def test_numero_entero(self):
        assert datos.agrega_decimales("100") == "100,00"

    def test_numero_con_punto(self):
        assert datos.agrega_decimales("1234.5") == "1.234,50"

    def test_numero_con_coma(self):
        assert datos.agrega_decimales("1234,5") == "1.234,50"

    def test_formato_argentino_entrada(self):
        """Entrada en formato 1234,56 (coma decimal) debe funcionar."""
        assert datos.agrega_decimales("1234,56") == "1.234,56"

    def test_formato_argentino_con_miles(self):
        """Entrada en formato 1.234,56 (miles con punto) debe funcionar."""
        assert datos.agrega_decimales("1.234,56") == "1.234,56"

    def test_valor_invalido(self):
        assert datos.agrega_decimales("abc") == "0,00"

    def test_redondeo(self):
        """1234.567 se redondea a 2 decimales."""
        assert datos.agrega_decimales("1234.567") == "1.234,57"

    def test_cero(self):
        assert datos.agrega_decimales("0") == "0,00"
        assert datos.agrega_decimales("0,5") == "0,50"


class TestGenHtml:
    """Tests para datos.gen_html."""

    def test_contiene_datos(self):
        html = datos.gen_html(
            "Escribanía Test",
            "Calle 1",
            "Tel 123",
            "Partes",
            "100,00",
            "30,00",
            "700,00",
            "5,40",
            "0,30",
            "1,00",
            "0,20",
            "1.000,00",
            "837,90",
            "Otros:",
            "0,00",
            "Otros:",
            "0,00",
            "Otros:",
            "0,00",
            "Escritura de Venta",
        )
        assert "Escribanía Test" in html
        assert "100,00" in html
        assert "Escritura de Venta" in html
        assert "<html>" in html
        assert "<body>" in html
        assert "Total:" in html

    def test_incluye_otros_si_no_cero(self):
        html = datos.gen_html(
            "E", "D", "T", "P",
            "100", "30", "700", "5", "0", "1", "0", "1000", "837",
            "Gastos:", "50,00", "Otros:", "0,00", "Otros:", "0,00",
            "Venta",
        )
        assert "Gastos:" in html
        assert "50,00" in html


class TestGenHtmlDonacion:
    """Tests para datos.gen_html_donacion."""

    def test_sin_reposicion(self):
        html = datos.gen_html_donacion(
            "E", "D", "T", "P",
            "100", "30", "700", "5", "0",
            "0", "1000", "837",
            "Otros:", "0", "Otros:", "0", "Otros:", "0",
        )
        assert "Donación" in html
        assert "Reposición" not in html
