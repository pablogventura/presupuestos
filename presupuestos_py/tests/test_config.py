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


def test_config_set_and_get():
    """set_value persiste y get recupera."""
    import config

    with tempfile.TemporaryDirectory() as tmp:
        path = os.path.join(tmp, "presupuestos.ini")
        with patch.object(config, "_get_config_path", return_value=path):
            config.set_value("Escribania", "Nombre", "Test Escribanía")
            assert config.get("Escribania", "Nombre") == "Test Escribanía"
