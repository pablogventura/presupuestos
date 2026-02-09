"""
Clase base para formularios de presupuesto (Venta, Donación, Cesión, Partición).
"""
import logging
import tkinter as tk

logger = logging.getLogger(__name__)
from tkinter import ttk, messagebox, filedialog

import config
from utils import centrar_ventana
import datos
import formatos


class BasePresupuestoWindow:
    TIPO_OPERACION = ""
    TIENE_REPOSICION = True
    USA_GEN_HTML = "gen"  # "gen" o "gen_donacion"

    def __init__(self, root: tk.Tk, on_volver):
        self.root = root
        self.on_volver = on_volver
        self.win = tk.Toplevel(root)
        self.win.title(self.TIPO_OPERACION)
        self.win.resizable(False, False)
        self.win.protocol("WM_DELETE_WINDOW", self._on_salir)

        self.aplicadamitad = False
        self._calculado = False
        self.entries = {}  # nombre -> Entry

        # Menú
        menubar = tk.Menu(self.win)
        self.win.config(menu=menubar)
        menu_archivo = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Archivo", menu=menu_archivo)
        menu_archivo.add_command(label="Exportar HTML...", command=self._exportar_html)
        menu_archivo.add_command(label="Guardar PDF como...", command=self._guardar_pdf)
        menu_archivo.add_command(label="Salir", command=self._on_salir)
        menu_edicion = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Edición", menu=menu_edicion)
        menu_edicion.add_command(label="Copiar resultados en HTML", command=self._copiar_html)
        menu_edicion.add_command(label="Pegar Valor Económico", command=self._pegar_ve)
        menu_edicion.add_command(label="Borrar todo", command=self._borrar_todo)
        menu_ayuda = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Ayuda", menu=menu_ayuda)
        menu_ayuda.add_command(label="Configuración", command=self._config)
        menu_ayuda.add_command(label="Acerca de...", command=self._about)

        # Valor económico
        frame_ve = ttk.LabelFrame(self.win, text="Valor económico:", padding=5)
        frame_ve.pack(fill=tk.X, padx=10, pady=5)
        self.veconomico = ttk.Entry(frame_ve, width=15)
        self.veconomico.insert(0, "0,00")
        self.veconomico.pack(anchor=tk.W)
        self.veconomico.bind("<FocusIn>", lambda e: self.veconomico.select_range(0, tk.END))
        self.veconomico.bind("<FocusOut>", self._on_ve_focusout)
        self.veconomico.bind("<Return>", self._on_return)
        self._lbl_ve_error = ttk.Label(frame_ve, text="", foreground="red")
        self._lbl_ve_error.pack(anchor=tk.W)

        # Atajos de teclado globales
        self.win.bind("<Control-s>", self._on_ctrl_s)
        self.win.bind("<Control-q>", self._on_ctrl_q)
        self.win.bind("<Return>", self._on_return)

        # Partes + Calcular
        frame_top = ttk.Frame(self.win, padding=5)
        frame_top.pack(fill=tk.X)
        frame_partes = ttk.LabelFrame(frame_top, text="Partes:", padding=5)
        frame_partes.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.partes = ttk.Entry(frame_partes, width=35)
        self.partes.pack(fill=tk.X)
        self.partes.bind("<Return>", self._on_return)
        ttk.Button(frame_top, text="Calcular", command=self._calcular).pack(
            side=tk.RIGHT, padx=5
        )

        # Presupuesto
        frame_pre = ttk.LabelFrame(self.win, text="Presupuesto:", padding=10)
        frame_pre.pack(fill=tk.X, padx=10, pady=5)

        rows = [
            ("Arancel:", "arancel"),
            ("Certificados:", "certificado"),
            ("Aportes (a):", "aportes1"),
            ("Aportes (b):", "aportes2"),
        ]
        if self.TIENE_REPOSICION:
            rows.append(("Reposición:", "reposicion"))
        rows.extend([
            ("Anotación:", "anotacion"),
            ("Gasto operativo:", "goperativo"),
            ("Protocolo Ley 9343:", "protoley"),
        ])
        for r, (label, key) in enumerate(rows):
            ttk.Label(frame_pre, text=label, width=20, anchor=tk.E).grid(
                row=r, column=0, sticky=tk.E, pady=2, padx=(0, 5)
            )
            e = ttk.Entry(frame_pre, width=12, state="disabled")
            e.insert(0, "0,00")
            e.grid(row=r, column=1, sticky=tk.W, pady=2)
            self.entries[key] = e

        # Bajar arancel
        r = len(rows)
        self.btn_bajar = tk.Button(
            frame_pre, text="/", width=2, bg="#c0c0c0",
            command=self._bajar_arancel, state="disabled"
        )
        self.btn_bajar.grid(row=0, column=2, padx=5)

        # Otros 1, 2, 3
        for i in range(1, 4):
            r += 1
            ne = ttk.Entry(frame_pre, width=15, state="disabled")
            ne.insert(0, "Otros:")
            ne.grid(row=r, column=0, sticky=tk.E, pady=2, padx=(0, 5))
            self.entries[f"notros{i}"] = ne
            oe = ttk.Entry(frame_pre, width=12, state="disabled")
            oe.insert(0, "0,00")
            oe.grid(row=r, column=1, sticky=tk.W, pady=2)
            self.entries[f"otros{i}"] = oe

        # Total
        r += 1
        ttk.Label(frame_pre, text="Total:", width=20, anchor=tk.E, font=("", 10, "bold")).grid(
            row=r, column=0, sticky=tk.E, pady=5, padx=(0, 5)
        )
        self.entries["total"] = ttk.Entry(frame_pre, width=12, state="disabled")
        self.entries["total"].insert(0, "0,00")
        self.entries["total"].grid(row=r, column=1, sticky=tk.W, pady=5)

        # Atajos para los entries más usados
        self.arancel = self.entries["arancel"]
        self.certificado = self.entries["certificado"]
        self.aportes1 = self.entries["aportes1"]
        self.aportes2 = self.entries["aportes2"]
        self.anotacion = self.entries["anotacion"]
        self.goperativo = self.entries["goperativo"]
        self.protoley = self.entries["protoley"]
        self.otros1 = self.entries["otros1"]
        self.otros2 = self.entries["otros2"]
        self.otros3 = self.entries["otros3"]
        self.total = self.entries["total"]
        if self.TIENE_REPOSICION:
            self.reposicion = self.entries["reposicion"]
        self.notros1 = self.entries["notros1"]
        self.notros2 = self.entries["notros2"]
        self.notros3 = self.entries["notros3"]

        # Recalcular Total al editar campos (tras Calcular)
        for key in ("arancel", "certificado", "aportes1", "aportes2", "anotacion",
                    "goperativo", "protoley", "otros1", "otros2", "otros3"):
            if key in self.entries:
                self.entries[key].bind("<FocusOut>", self._actualizar_total)
        if self.TIENE_REPOSICION and "reposicion" in self.entries:
            self.entries["reposicion"].bind("<FocusOut>", self._actualizar_total)

        # Botón Imprimir
        r += 1
        ttk.Button(frame_pre, text="Imprimir (PDF)", command=self._imprimir).grid(
            row=r, column=0, columnspan=2, sticky=tk.W, pady=10
        )

    def _get_ve(self) -> float:
        return formatos.parse_decimal(self.veconomico.get())

    def _on_return(self, event=None):
        """Enter: valor económico → partes → calcular → imprimir."""
        focus = self.win.focus_get()
        if focus == self.veconomico:
            self.partes.focus_set()
            return "break"
        if focus == self.partes:
            self._calcular()
            return "break"
        # Tras calcular, Enter en cualquier campo → imprimir
        if self._calculado:
            self._imprimir()
            return "break"

    def _on_ve_focusout(self, event=None):
        """Valida Valor económico al perder foco."""
        val = self.veconomico.get().strip()
        if not val:
            self._lbl_ve_error.config(text="")
            return
        v = formatos.parse_decimal(val)
        if v == 0 and val.lower() not in ("0", "0,00", "0.00", "0,0", "0.0"):
            self._lbl_ve_error.config(text="Valor no numérico")
        else:
            self._lbl_ve_error.config(text="")

    def _on_ctrl_s(self, event):
        self._exportar_html()
        return "break"

    def _on_ctrl_q(self, event):
        self._on_salir()
        return "break"

    def _actualizar_total(self, event=None):
        """Actualiza el Total si los campos de monto están habilitados."""
        st = str(self.total.cget("state"))
        habilitado = "normal" in st and "disabled" not in st
        if habilitado:
            self.total.delete(0, tk.END)
            self.total.insert(0, self._sumar_todo())

    def _set_entry(self, key: str, valor: str):
        e = self.entries.get(key)
        if e:
            e.config(state="normal")
            e.delete(0, tk.END)
            e.insert(0, valor)
            e.config(state="disabled")

    def _calcular_base(self, ve: float) -> dict:
        """
        Calcula valores del presupuesto según valor económico.
        Devuelve dict con arancel, certificado, aportes1, aportes2,
        reposicion (si aplica), anotacion, goperativo, protoley.
        """
        d = config.get_presupuesto_defaults()
        arancel = ve * d["tasa_arancel"] + d["arancel_fijo"]
        vals = {
            "arancel": datos.agrega_decimales(arancel),
            "certificado": formatos.formatear_decimal(d["certificado_base"]),
            "aportes1": datos.agrega_decimales((arancel / 2) * 0.18),
            "aportes2": datos.agrega_decimales(ve * d["aportes2_porcentaje"]),
            "anotacion": datos.agrega_decimales(max(ve * d["anotacion_porcentaje"], d["anotacion_minimo"])),
            "goperativo": formatos.formatear_decimal(d["goperativo"]),
            "protoley": formatos.formatear_decimal(d["protoley"]),
        }
        if self.TIENE_REPOSICION:
            vals["reposicion"] = datos.agrega_decimales(
                max(ve * d["reposicion_porcentaje"], d["reposicion_minimo"])
            )
        return vals

    def _validar_otros(self) -> bool:
        """Valida que los campos 'otros' sean numéricos. Retorna True si hay error."""
        for i in (1, 2, 3):
            formatos.parse_decimal(self.entries[f"otros{i}"].get())
        return False

    def _calcular(self):
        """Override en subclases si necesitan lógica específica."""
        pass

    def _aplicar_calculo(self, ve: float) -> None:
        """Aplica valores calculados a los campos y habilita edición."""
        self._calculado = True
        vals = self._calcular_base(ve)
        self.veconomico.delete(0, tk.END)
        self.veconomico.insert(0, formatos.formatear_decimal(ve))
        for key, valor in vals.items():
            self._set_entry(key, valor)
        self._set_entry("total", self._sumar_todo())
        self._habilitar_campos()
        self.total.focus_set()

    def _sumar_todo(self) -> str:
        total_val = formatos.parse_decimal(self.arancel.get()) + formatos.parse_decimal(self.certificado.get())
        total_val += formatos.parse_decimal(self.aportes1.get()) + formatos.parse_decimal(self.aportes2.get())
        total_val += formatos.parse_decimal(self.anotacion.get()) + formatos.parse_decimal(self.goperativo.get())
        total_val += formatos.parse_decimal(self.protoley.get())
        total_val += formatos.parse_decimal(self.otros1.get()) + formatos.parse_decimal(self.otros2.get()) + formatos.parse_decimal(self.otros3.get())
        if self.TIENE_REPOSICION:
            total_val += formatos.parse_decimal(self.reposicion.get())
        return formatos.formatear_decimal(total_val)

    def _habilitar_campos(self):
        for key in ("arancel", "certificado", "aportes1", "aportes2", "anotacion",
                    "goperativo", "protoley", "otros1", "otros2", "otros3", "total"):
            if key in self.entries:
                self.entries[key].config(state="normal")
        if self.TIENE_REPOSICION and "reposicion" in self.entries:
            self.entries["reposicion"].config(state="normal")
        self.partes.config(state="normal")
        self.btn_bajar.config(state="normal")

    def _bajar_arancel(self):
        if not self.aplicadamitad:
            val = formatos.parse_decimal(self.arancel.get()) / 2
            self._set_entry("arancel", formatos.formatear_decimal(val))
            self.total.delete(0, tk.END)
            self.total.insert(0, self._sumar_todo())
            self.aplicadamitad = True
            self.btn_bajar.config(bg="red")

    def _exportar_html(self):
        html = self._get_html()
        if not html:
            return
        path = filedialog.asksaveasfilename(
            defaultextension=".htm",
            filetypes=[("Página Web (*.htm)", "*.htm"), ("Todos", "*.*")],
        )
        if path:
            try:
                with open(path, "w", encoding="utf-8") as f:
                    f.write(html)
                logger.info("HTML exportado: %s", path)
                messagebox.showinfo("Exportar HTML", "Archivo guardado correctamente.")
            except OSError as e:
                logger.error("Error al exportar HTML: %s", e)
                messagebox.showerror("Error", f"No se pudo guardar el archivo.\n\n{e}")

    def _copiar_html(self):
        html = self._get_html()
        if html:
            self.win.clipboard_clear()
            self.win.clipboard_append(html)
            messagebox.showinfo("Copiar", "HTML copiado al portapapeles.")

    def _get_html(self) -> str:
        """Override en subclases según USA_GEN_HTML."""
        return ""

    def _pegar_ve(self):
        try:
            txt = self.win.clipboard_get()
            self.veconomico.delete(0, tk.END)
            self.veconomico.insert(0, txt.strip())
        except tk.TclError:
            pass

    def _borrar_todo(self):
        self._calculado = False
        self.veconomico.delete(0, tk.END)
        self.veconomico.insert(0, "0,00")
        self.partes.config(state="normal")
        self.partes.delete(0, tk.END)
        for key, e in self.entries.items():
            if key.startswith("notros"):
                e.config(state="normal")
                e.delete(0, tk.END)
                e.insert(0, "Otros:")
                e.config(state="disabled")
            elif key.startswith("otros") or key in ("arancel", "certificado", "aportes1", "aportes2",
                                                     "anotacion", "goperativo", "protoley", "total"):
                e.config(state="normal")
                e.delete(0, tk.END)
                e.insert(0, "0,00")
                e.config(state="disabled")
            elif key == "reposicion" and self.TIENE_REPOSICION:
                e.config(state="normal")
                e.delete(0, tk.END)
                e.insert(0, "0,00")
                e.config(state="disabled")
        self.aplicadamitad = False
        self.btn_bajar.config(bg="#c0c0c0", state="disabled")
        self.veconomico.focus_set()

    def _imprimir(self):
        """Override en subclases para llamar a impresion."""
        pass

    def _imprimir_a_archivo(self, path: str) -> None:
        """Override en subclases: genera PDF en path."""
        pass

    def _guardar_pdf(self) -> None:
        """Diálogo Guardar PDF como."""
        path = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF (*.pdf)", "*.pdf"), ("Todos", "*.*")],
        )
        if path:
            self._imprimir_a_archivo(path)
            messagebox.showinfo("Guardar PDF", "Archivo guardado correctamente.")

    def _config(self):
        from ui.configuracion import ConfiguracionDialog
        ConfiguracionDialog(self.win)

    def _about(self):
        from ui.about import AboutDialog
        AboutDialog(self.win)

    def _on_salir(self):
        self.win.destroy()
        self.on_volver()

    def show(self):
        centrar_ventana(self.win)
        self.win.deiconify()
        self.win.lift()
        self.win.focus_force()
        self.veconomico.focus_set()
