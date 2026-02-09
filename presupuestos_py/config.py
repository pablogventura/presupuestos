"""
Configuración de Presupuestos.
El archivo presupuestos.ini se guarda en el directorio del ejecutable.
"""
import configparser
import os
import sys

CONFIG_FILENAME = "presupuestos.ini"
DEFAULT_VALUES = {
    "Escribania": {
        "Nombre": "Ventura",
        "Direccion": 'Corrientes 5 - 4º "A"',
        "Telefonoemail": "Te: 4255715 - e-mail: gabventura@arnet.com.ar",
    },
    "Impresion": {
        "MargenSuperior": "4000",
    },
}


def _get_config_dir() -> str:
    """Obtiene el directorio donde guardar/cargar la configuración."""
    if getattr(sys, "frozen", False):
        return os.path.dirname(sys.executable)
    return os.path.dirname(os.path.abspath(__file__))


def _get_config_path() -> str:
    return os.path.join(_get_config_dir(), CONFIG_FILENAME)


def get(section: str, key: str, default: str = "") -> str:
    """Obtiene un valor de configuración."""
    cfg = configparser.ConfigParser()
    path = _get_config_path()
    if os.path.exists(path):
        cfg.read(path, encoding="utf-8")
    if section in cfg and key in cfg[section]:
        return cfg[section][key]
    if section in DEFAULT_VALUES and key in DEFAULT_VALUES[section]:
        return DEFAULT_VALUES[section][key]
    return default if default else ""


def set_value(section: str, key: str, value: str) -> None:
    """Guarda un valor de configuración."""
    cfg = configparser.ConfigParser()
    path = _get_config_path()
    if os.path.exists(path):
        cfg.read(path, encoding="utf-8")
    if section not in cfg:
        cfg[section] = {}
    cfg[section][key] = value
    with open(path, "w", encoding="utf-8") as f:
        cfg.write(f)
