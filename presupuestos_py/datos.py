"""
Módulo de datos: formato decimal con coma y generación HTML.
Migrado desde Module1.bas (Datos).
"""
from pathlib import Path

import formatos
from jinja2 import Environment, FileSystemLoader


def agrega_decimales(numero) -> str:
    """
    Formatea un número con coma decimal y siempre 2 decimales.
    Acepta float o string (incl. formato argentino "1.234,56").
    Ej: 1234.5 -> "1.234,50"
    """
    return formatos.formatear_decimal(numero)


def _cargar_plantilla(nombre: str):
    """Carga la plantilla Jinja2."""
    ruta = Path(__file__).parent / "templates"
    env = Environment(loader=FileSystemLoader(str(ruta)), autoescape=True)
    return env.get_template(nombre)


def gen_html(
    escribania: str,
    direccion: str,
    telefono: str,
    partes: str,
    v_economico: str,
    arancel: str,
    certificados: str,
    aportes1: str,
    aportes2: str,
    reposicion: str,
    anotacion: str,
    goperativo: str,
    total: str,
    notros1: str,
    otros1: str,
    notros2: str,
    otros2: str,
    notros3: str,
    otros3: str,
    tipo_operacion: str,
) -> str:
    """Genera HTML del presupuesto (Venta, Cesión, etc.)."""
    otros = []
    for nom, val in [(notros1, otros1), (notros2, otros2), (notros3, otros3)]:
        if val != "0,00":
            otros.append({"nombre": nom, "valor": val})
    return _cargar_plantilla("presupuesto_venta.html").render(
        escribania=escribania,
        direccion=direccion,
        telefono=telefono,
        partes=partes,
        v_economico=v_economico,
        arancel=arancel,
        certificados=certificados,
        aportes1=aportes1,
        aportes2=aportes2,
        reposicion=reposicion,
        anotacion=anotacion,
        goperativo=goperativo,
        total=total,
        otros=otros,
        tiene_reposicion=True,
        tipo_operacion=tipo_operacion,
    )


def gen_html_donacion(
    escribania: str,
    direccion: str,
    telefono: str,
    partes: str,
    v_economico: str,
    arancel: str,
    certificados: str,
    aportes1: str,
    aportes2: str,
    anotacion: str,
    goperativo: str,
    total: str,
    notros1: str,
    otros1: str,
    notros2: str,
    otros2: str,
    notros3: str,
    otros3: str,
) -> str:
    """Genera HTML del presupuesto de Donación (sin reposición)."""
    otros = []
    for nom, val in [(notros1, otros1), (notros2, otros2), (notros3, otros3)]:
        if val != "0,00":
            otros.append({"nombre": nom, "valor": val})
    return _cargar_plantilla("presupuesto_venta.html").render(
        escribania=escribania,
        direccion=direccion,
        telefono=telefono,
        partes=partes,
        v_economico=v_economico,
        arancel=arancel,
        certificados=certificados,
        aportes1=aportes1,
        aportes2=aportes2,
        reposicion="0,00",
        anotacion=anotacion,
        goperativo=goperativo,
        total=total,
        otros=otros,
        tiene_reposicion=False,
        tipo_operacion="Donación",
    )
