"""
Configuración de Presupuestos.
El archivo presupuestos.ini se guarda en el directorio del ejecutable.
"""
import configparser
import os
import sys

import formatos

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
    "Presupuesto": {
        "certificado_base": "700",
        "goperativo": "1000",
        "protoley": "150",
        "tasa_arancel": "0.02",
        "arancel_fijo": "27.7",
        "reposicion_minimo": "30",
        "reposicion_porcentaje": "0.01",
        "anotacion_minimo": "30",
        "anotacion_porcentaje": "0.002",
        "aportes2_porcentaje": "0.003",
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


def get_escribania() -> dict:
    """Devuelve nombre, direccion y telefono de la escribanía."""
    return {
        "nombre": get("Escribania", "Nombre", "Ventura"),
        "direccion": get(
            "Escribania",
            "Direccion",
            'Corrientes 5 - 4º "A"',
        ),
        "telefono": get(
            "Escribania",
            "Telefonoemail",
            "Te: 4255715 - e-mail: gabventura@arnet.com.ar",
        ),
    }


def get_presupuesto_defaults() -> dict:
    """Devuelve constantes de presupuesto (certificado_base, goperativo, etc.)."""
    def _f(key: str, default: str) -> float:
        return formatos.parse_decimal(get("Presupuesto", key, default))

    return {
        "certificado_base": _f("certificado_base", "700"),
        "goperativo": _f("goperativo", "1000"),
        "protoley": _f("protoley", "150"),
        "tasa_arancel": _f("tasa_arancel", "0.02"),
        "arancel_fijo": _f("arancel_fijo", "27.7"),
        "reposicion_minimo": _f("reposicion_minimo", "30"),
        "reposicion_porcentaje": _f("reposicion_porcentaje", "0.01"),
        "anotacion_minimo": _f("anotacion_minimo", "30"),
        "anotacion_porcentaje": _f("anotacion_porcentaje", "0.002"),
        "aportes2_porcentaje": _f("aportes2_porcentaje", "0.003"),
    }


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
