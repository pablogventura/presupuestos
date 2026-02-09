"""
Impresión: genera PDF con ReportLab y lo abre en el visor del sistema.
Migrado desde Module2.bas (Impresion).
"""
import os
import subprocess
import sys
import tempfile

import config
import formatos

# Twips a points: 1440 twips = 1 inch, 72 points = 1 inch => 1 twip = 72/1440 = 0.05 pts
TWIPS_TO_POINTS = 72 / 1440


def _twips_to_pts(twips: float) -> float:
    return float(twips) * TWIPS_TO_POINTS


def _abrir_pdf(ruta: str) -> bool:
    """Abre el PDF en el visor por defecto. Devuelve True si ok, False si falló."""
    try:
        if sys.platform == "win32":
            os.startfile(ruta)
        elif sys.platform == "darwin":
            subprocess.run(["open", ruta], check=False)
        else:
            subprocess.run(["xdg-open", ruta], check=False)
        return True
    except Exception:
        return False


def _escribir(canvas, texto: str, fuente: str, tamano: float, posx: str, y: float, alineacion: int = 2):
    """Dibuja texto en el canvas PDF."""
    canvas.setFont("Times-Roman", tamano)
    w = canvas._pagesize[0]
    if posx == "centro":
        x = w / 2
    elif posx == "tercio":
        x = w / 3
    elif posx == "terciod":
        x = (w / 3) * 2
    else:
        x = float(posx)
    tw = canvas.stringWidth(texto, "Times-Roman", tamano)
    if alineacion == 2:  # centrado
        x -= tw / 2
    elif alineacion == 3:  # derecha
        x -= tw
    canvas.drawString(x, y, texto)


def _generar_pdf(
    titulo: str,
    partes: str,
    v_economico: str,
    arancel: str,
    certificado: str,
    aportes1: str,
    aportes2: str,
    anotacion: str,
    goperativo: str,
    protoley: str,
    otros1: str,
    otros2: str,
    otros3: str,
    notros1: str,
    notros2: str,
    notros3: str,
    total: str,
    bajar_arancel: bool,
    tiene_reposicion: bool,
    reposicion: str = "0,00",
) -> str:
    """Genera el PDF y devuelve la ruta del archivo."""
    from reportlab.lib.pagesizes import A4
    from reportlab.pdfgen import canvas

    esc = config.get_escribania()
    nombre = esc["nombre"]
    direccion = esc["direccion"]
    telefono = esc["telefono"]
    margen = _twips_to_pts(config.get("Impresion", "MargenSuperior", "4000"))

    f, ruta = tempfile.mkstemp(suffix=".pdf")
    os.close(f)
    c = canvas.Canvas(ruta, pagesize=A4)
    ancho, alto = A4
    # Origen abajo-izquierda
    y = alto - margen

    escribania_txt = ("Escribanía" if bajar_arancel else "Escribanía ") + nombre

    _escribir(c, escribania_txt, "Times-Roman", 18, "centro", y)
    y -= 20
    _escribir(c, direccion, "Times-Roman", 12, "centro", y)
    y -= 15
    _escribir(c, telefono, "Times-Roman", 12, "centro", y)
    y -= 25
    _escribir(c, titulo, "Times-Roman", 16, "centro", y)
    if partes:
        y -= 20
        _escribir(c, partes, "Times-Roman", 14, "centro", y)
        y -= 25
    else:
        y -= 20

    def fila(etiqueta: str, valor: str):
        nonlocal y
        _escribir(c, etiqueta, "Times-Roman", 12, "tercio", y, 3)
        _escribir(c, "$", "Times-Roman", 12, "centro", y, 3)
        _escribir(c, valor, "Times-Roman", 12, "terciod", y, 3)
        y -= 18

    fila("Valor económico:", v_economico)
    fila("Arancel:", arancel)
    fila("Certificados:", certificado)
    fila("Aportes (a):", aportes1)
    fila("Aportes (b):", aportes2)
    if tiene_reposicion:
        fila("Reposición:", reposicion)
    fila("Anotación:", anotacion)
    fila("Gasto operativo:", goperativo)
    fila("Protocolo Ley 9343:", protoley)
    if formatos.parse_decimal(otros1) != 0:
        fila(notros1, otros1)
    if formatos.parse_decimal(otros2) != 0:
        fila(notros2, otros2)
    if formatos.parse_decimal(otros3) != 0:
        fila(notros3, otros3)
    y -= 5
    fila("Total:", total)

    c.save()
    return ruta


def dibujar_venta(
    arancel, certificado, aportes1, aportes2, reposicion, anotacion,
    goperativo, protoley, otros1, otros2, otros3,
    notros1, notros2, notros3, total, partes, v_economico, bajar_arancel,
):
    ruta = _generar_pdf(
        "Presupuesto - Escritura de Venta",
        partes, v_economico, arancel, certificado,
        aportes1, aportes2, anotacion, goperativo, protoley,
        otros1, otros2, otros3, notros1, notros2, notros3, total,
        bajar_arancel, True, reposicion,
    )
    if not _abrir_pdf(ruta):
        from tkinter import messagebox
        messagebox.showwarning(
            "PDF generado",
            f"No se pudo abrir el visor de PDF.\n\nEl archivo se guardó en:\n{ruta}",
        )


def dibujar_donacion(
    arancel, certificado, aportes1, aportes2, anotacion, goperativo,
    protoley, otros1, otros2, otros3, notros1, notros2, notros3,
    total, partes, v_economico, bajar_arancel,
):
    ruta = _generar_pdf(
        "Presupuesto - Donación",
        partes, v_economico, arancel, certificado,
        aportes1, aportes2, anotacion, goperativo, protoley,
        otros1, otros2, otros3, notros1, notros2, notros3, total,
        bajar_arancel, False,
    )
    if not _abrir_pdf(ruta):
        from tkinter import messagebox
        messagebox.showwarning(
            "PDF generado",
            f"No se pudo abrir el visor de PDF.\n\nEl archivo se guardó en:\n{ruta}",
        )


def dibujar_cesion(
    arancel, certificado, aportes1, aportes2, reposicion, anotacion,
    goperativo, protoley, otros1, otros2, otros3,
    notros1, notros2, notros3, total, partes, v_economico, bajar_arancel,
):
    ruta = _generar_pdf(
        "Presupuesto - Escritura de Cesión de Derechos Onerosa",
        partes, v_economico, arancel, certificado,
        aportes1, aportes2, anotacion, goperativo, protoley,
        otros1, otros2, otros3, notros1, notros2, notros3, total,
        bajar_arancel, True, reposicion,
    )
    if not _abrir_pdf(ruta):
        from tkinter import messagebox
        messagebox.showwarning(
            "PDF generado",
            f"No se pudo abrir el visor de PDF.\n\nEl archivo se guardó en:\n{ruta}",
        )


def dibujar_particion(
    arancel, certificado, aportes1, aportes2, anotacion, goperativo,
    protoley, otros1, otros2, otros3, notros1, notros2, notros3,
    total, partes, v_economico, bajar_arancel,
):
    ruta = _generar_pdf(
        "Presupuesto - Partición o Adjudicación",
        partes, v_economico, arancel, certificado,
        aportes1, aportes2, anotacion, goperativo, protoley,
        otros1, otros2, otros3, notros1, notros2, notros3, total,
        bajar_arancel, False,
    )
    if not _abrir_pdf(ruta):
        from tkinter import messagebox
        messagebox.showwarning(
            "PDF generado",
            f"No se pudo abrir el visor de PDF.\n\nEl archivo se guardó en:\n{ruta}",
        )
