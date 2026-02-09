"""
Presupuestos - Punto de entrada.
Migrado desde VB6 Presupuestos.
"""
import logging
import os

logging.basicConfig(level=logging.WARNING, format="%(name)s: %(message)s")
import tkinter as tk
from tkinter import messagebox

from ui.principal import PrincipalWindow
from utils import VERSION, get_icon_path


def show_splash(root: tk.Tk):
    """Muestra splash 750ms y luego la ventana principal."""
    splash = tk.Toplevel(root)
    splash.title("Presupuestos")
    splash.resizable(False, False)
    splash.overrideredirect(True)

    # Centrar
    w, h = 468, 350
    x = (splash.winfo_screenwidth() - w) // 2
    y = (splash.winfo_screenheight() - h) // 2
    splash.geometry(f"{w}x{h}+{x}+{y}")

    frame = tk.Frame(splash, padx=20, pady=20)
    frame.pack(fill=tk.BOTH, expand=True)

    tk.Label(frame, text="Presupuestos", font=("Arial", 24, "bold")).pack(anchor=tk.W)
    tk.Label(frame, text=f"Versión {VERSION}", font=("Arial", 12, "bold")).pack(anchor=tk.E)
    tk.Label(frame, text="© Pablo Ventura 2003-2026", font=("Arial", 8)).pack(side=tk.BOTTOM, anchor=tk.W)

    # Icono
    try:
        icon_path = get_icon_path()
        if os.path.exists(icon_path):
            img = tk.PhotoImage(file=icon_path)
            lbl = tk.Label(frame, image=img)
            lbl.image = img
            lbl.pack(pady=10)
    except Exception:
        pass

    def on_timer():
        splash.destroy()
        principal = PrincipalWindow(root)
        principal.show()

    splash.after(750, on_timer)


def main():
    root = tk.Tk()
    root.withdraw()

    # Icono de la app
    try:
        import platform

        icon_path = get_icon_path()
        if os.path.exists(icon_path):
            if platform.system() == "Windows":
                root.iconbitmap(icon_path)
            else:
                img = tk.PhotoImage(file=icon_path)
                root.iconphoto(True, img)
    except Exception:
        pass

    show_splash(root)
    root.mainloop()


if __name__ == "__main__":
    main()
