"""
Utilidades: rutas de assets, detección de plataforma.
"""
import os
import sys

VERSION = "6.0.0"


def get_asset_path(filename: str) -> str:
    """Obtiene la ruta a un archivo en assets/."""
    if getattr(sys, "frozen", False):
        base = sys._MEIPASS
    else:
        base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base, "assets", filename)


def centrar_ventana(win) -> None:
    """Centra una ventana Toplevel en la pantalla."""
    win.update_idletasks()
    w = win.winfo_reqwidth()
    h = win.winfo_reqheight()
    x = (win.winfo_screenwidth() - w) // 2
    y = (win.winfo_screenheight() - h) // 2
    win.geometry(f"+{x}+{y}")


def get_icon_path() -> str:
    """Devuelve la ruta del icono según plataforma (.ico Windows, .png Linux)."""
    import platform

    if platform.system() == "Windows":
        return get_asset_path("icono.ico")
    return get_asset_path("icono.png")
