"""
Formato decimal: parseo y formateo con coma decimal (formato argentino).
Centraliza la lógica usada en datos, impresion y base_presupuesto.
"""


def parse_decimal(s: str) -> float:
    """
    Convierte string con formato argentino (1.234,56) a float.
    Acepta: "1.234,56", "1234,56", "1234.56", "1234"
    """
    try:
        t = str(s).strip()
        if not t:
            return 0.0
        # Quitar separador de miles (punto), coma como decimal
        t = t.replace(".", "").replace(",", ".")
        return float(t)
    except ValueError:
        return 0.0


def formatear_decimal(valor) -> str:
    """
    Formatea un número con coma decimal y siempre 2 decimales.
    Acepta float o string (ej: 1234.5, "1.234,50").
    Ej: 1234.5 -> "1.234,50"
    """
    if isinstance(valor, (int, float)):
        num = float(valor)
    else:
        num = parse_decimal(str(valor))
    redondeado = round(num, 2)
    partes = f"{redondeado:.2f}".split(".")
    entero = partes[0]
    decimal = partes[1]
    # Formato argentino: miles con punto, decimales con coma
    if len(entero) > 3:
        entero_formateado = ""
        for i, c in enumerate(reversed(entero)):
            if i > 0 and i % 3 == 0:
                entero_formateado = "." + entero_formateado
            entero_formateado = c + entero_formateado
        entero = entero_formateado
    return f"{entero},{decimal}"
