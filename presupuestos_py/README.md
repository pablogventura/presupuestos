# Presupuestos (Python)

Migración de la aplicación Presupuestos desde Visual Basic 6 a Python con Tkinter.

## Requisitos

- Python 3.10+
- ReportLab
- Pillow (para iconos)

## Instalación y ejecución

### Con entorno virtual (recomendado)

```bash
cd presupuestos_py
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python main.py
```

### Ejecutar tests

```bash
.venv/bin/pytest tests/ -v
```

### Empaquetado con PyInstaller

```bash
.venv/bin/pip install pyinstaller
.venv/bin/pyinstaller build.spec
```

El ejecutable se generará en `dist/Presupuestos` (o `dist/Presupuestos.exe` en Windows).

## Plataformas

- **Windows**: usa icono.ico
- **Linux**: usa icono.png

La configuración se guarda en `presupuestos.ini` en el mismo directorio que el ejecutable.
