# Presupuestos - Build con PyInstaller
# Uso: make exe       → genera dist/Presupuestos.exe (Windows) o dist/Presupuestos
#      make deps      → instala dependencias
#      make clean     → borra build/ y dist/

PYINSTALLER = pyinstaller
SPEC = build.spec

.PHONY: exe build clean distclean deps

exe: build

deps:
	pip install -r requirements.txt

build:
	$(PYINSTALLER) $(SPEC)
	@echo "Listo. Ejecutable en dist/Presupuestos.exe (Windows) o dist/Presupuestos (Linux/macOS)"

clean:
	rm -rf build/
	rm -rf dist/

distclean: clean
	rm -rf __pycache__ ui/__pycache__ tests/__pycache__
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
