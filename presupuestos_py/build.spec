# -*- mode: python ; coding: utf-8 -*-
# PyInstaller spec para Presupuestos
# Ejecutar: pyinstaller build.spec

import sys
import os

block_cipher = None

# Icono según plataforma
is_win = sys.platform == 'win32'
icon_file = 'assets/icono.ico' if is_win else 'assets/icono.png'

# Asegurar que templates y jinja2 se incluyan
from PyInstaller.utils.hooks import collect_data_files

extra_datas = list(collect_data_files('jinja2', include_py_files=False))
if os.path.exists('templates'):
    extra_datas.append(('templates', 'templates'))

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('assets/icono.ico', 'assets'),
        ('assets/icono.png', 'assets'),
    ] + extra_datas,
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='Presupuestos',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=icon_file if os.path.exists(icon_file) else None,
)
