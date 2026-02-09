"""Tests para el módulo config."""
import os
import tempfile
from unittest.mock import patch

import pytest


def test_config_get_defaults():
    """Sin archivo, devuelve valores por defecto."""
    import config

    with patch.object(config, "_get_config_path", return_value="/no/existe/ini"):
        assert config.get("Escribania", "Nombre", "Ventura") == "Ventura"
        assert config.get("Impresion", "MargenSuperior", "4000") == "4000"


def test_get_escribania():
    """get_escribania devuelve dict con nombre, direccion, telefono."""
    import config

    with patch.object(config, "_get_config_path", return_value="/no/existe/ini"):
        esc = config.get_escribania()
        assert "nombre" in esc and "direccion" in esc and "telefono" in esc
        assert esc["nombre"] == "Ventura"


def test_get_presupuesto_defaults():
    """get_presupuesto_defaults devuelve constantes numéricas."""
    import config

    with patch.object(config, "_get_config_path", return_value="/no/existe/ini"):
        d = config.get_presupuesto_defaults()
        assert d["certificado_base"] == 700
        assert d["goperativo"] == 1000
        assert d["tasa_arancel"] == 0.02


def test_config_set_and_get():
    """set_value persiste y get recupera."""
    import config

    with tempfile.TemporaryDirectory() as tmp:
        path = os.path.join(tmp, "presupuestos.ini")
        with patch.object(config, "_get_config_path", return_value=path):
            config.set_value("Escribania", "Nombre", "Test Escribanía")
            assert config.get("Escribania", "Nombre") == "Test Escribanía"
