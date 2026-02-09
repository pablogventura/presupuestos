# Presupuestos

Aplicación de escritorio para generar presupuestos de escribanía. Migrada desde Visual Basic 6 a Python con Tkinter.

## Descripción

Permite calcular y exportar presupuestos para distintas operaciones notariales:

- **Venta** – Escritura de venta (con reposición)
- **Donación**
- **Cesión de derechos** – Cesión onerosa (con reposición)
- **Partición o adjudicación**

Incluye generación de PDF, exportación a HTML y formato decimal argentino (coma como separador decimal).

## Requisitos

- Python 3.10+
- ReportLab
- Pillow
- Jinja2

## Instalación

### Con entorno virtual (recomendado)

```bash
cd presupuestos_py
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
```

### Ejecución

```bash
.venv/bin/python main.py
```

## Uso

1. Elegir el tipo de operación (Venta, Donación, etc.).
2. Ingresar el **Valor económico** en formato argentino (ej: `100.000,00`).
3. Pulsar **Calcular**.
4. Opciones:
   - **Imprimir (PDF)** – Genera PDF y lo abre en el visor del sistema.
   - **Guardar PDF como...** – Guarda el PDF en la ubicación elegida.
   - **Exportar HTML...** – Exporta el presupuesto como página web.
   - **Copiar resultados en HTML** – Copia al portapapeles.

### Atajos de teclado

- **Enter** (en Valor económico) – Calcular
- **Ctrl+S** – Exportar HTML
- **Ctrl+Q** – Salir

## Configuración

Desde **Ayuda → Configuración** se puede ajustar:

- **Escribanía**: nombre, dirección, teléfono/e-mail
- **Impresión**: margen superior (en mm, pt o twips)
- Los parámetros de presupuesto se guardan en `presupuestos.ini`

El archivo de configuración se guarda en el mismo directorio que el ejecutable (o del script al ejecutar desde código).

## Tests

```bash
.venv/bin/python -m pytest tests/ -v
```

Incluye tests de cálculos, configuración, datos, impresión, integración y UI.

## Empaquetado

Para generar un ejecutable con PyInstaller:

```bash
.venv/bin/pip install pyinstaller
.venv/bin/pyinstaller build.spec
```

El ejecutable se genera en `dist/Presupuestos` (o `Presupuestos.exe` en Windows).

## Estructura del proyecto

```
presupuestos_py/
├── main.py           # Punto de entrada
├── config.py         # Configuración (INI)
├── datos.py          # Datos, formato decimal, HTML (Jinja2)
├── formatos.py       # Parseo y formateo decimal
├── impresion.py      # Generación de PDF
├── utils.py          # Utilidades, iconos
├── templates/        # Plantillas Jinja2 para HTML
├── ui/               # Interfaz Tkinter
│   ├── principal.py  # Menú principal
│   ├── base_presupuesto.py
│   ├── venta.py
│   ├── donacion.py
│   ├── cesiond.py
│   ├── particion.py
│   ├── configuracion.py
│   └── about.py
├── assets/           # Iconos
└── tests/            # Tests
```

## Plataformas

- **Windows**: icono `.ico`
- **Linux / macOS**: icono `.png`

## Licencia

© Pablo Ventura 2003-2026
