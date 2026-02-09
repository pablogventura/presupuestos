"""
Módulo de datos: formato decimal con coma y generación HTML.
Migrado desde Module1.bas (Datos).
"""


def agrega_decimales(numero: str) -> str:
    """
    Formatea un número con coma decimal y siempre 2 decimales.
    Ej: 1234.5 -> "1.234,50"
    """
    try:
        valor = float(str(numero).replace(",", "."))
    except ValueError:
        return "0,00"
    redondeado = round(valor, 2)
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
    q = '"'
    nl = "\n"
    s = f"""<html>{nl}{nl}<body>{nl}{nl}<p align={q}center{q}><font size={q}5{q}>{escribania}</font></p>{nl}<p align={q}center{q}><font size={q}4{q}>{direccion}</font></p>{nl}<p align={q}center{q}><font size={q}4{q}>{telefono}</font></p>{nl}<p align={q}center{q}><font size={q}4{q}>Presupuesto - {tipo_operacion}</font></p>{nl}<p align={q}center{q}>{partes}</p>{nl}<p align={q}center{q}>&nbsp;</p>{nl}<div align={q}center{q} style={q}width: 383; height: 209{q}>{nl}  <center>{nl}  <table border={q}1{q} cellpadding={q}0{q} cellspacing={q}0{q} style={q}border-collapse: collapse{q} bordercolor={q}#FFFFFF{q} width={q}256{q} height={q}1{q} id={q}AutoNumber1{q} align={q}right{q}>{nl}    <tr>{nl}      <td width={q}264{q} height={q}13{q} align={q}center{q}>{nl}      <p align={q}right{q}>Valor económico:</td>{nl}      <td width={q}79{q} height={q}13{q} align={q}center{q}>{nl}      <p align={q}right{q}><span lang={q}es{q}>$</span></td>{nl}      <td width={q}173{q} height={q}13{q} align={q}center{q}>{nl}      <p align={q}right{q}><span lang={q}es{q}>{v_economico}</span></td>{nl}    </tr>{nl}    <tr>{nl}      <td width={q}264{q} height={q}14{q} align={q}center{q}>{nl}      <p align={q}right{q}>Arancel:</td>{nl}      <td width={q}79{q} height={q}14{q} align={q}center{q}>{nl}      <p align={q}right{q}><span lang={q}es{q}>$</span></td>{nl}      <td width={q}173{q} height={q}14{q} align={q}center{q}>{nl}      <p align={q}right{q}><span lang={q}es{q}>{arancel}</span></td>{nl}    </tr>{nl}    <tr>{nl}      <td width={q}264{q} height={q}17{q} align={q}center{q}>{nl}      <p align={q}right{q}>Certificados:</td>{nl}      <td width={q}79{q} height={q}17{q} align={q}center{q}>{nl}      <p align={q}right{q}><span lang={q}es{q}>$</span></td>{nl}      <td width={q}173{q} height={q}17{q} align={q}center{q}>{nl}      <p align={q}right{q}><span lang={q}es{q}>{certificados}</span></td>{nl}    </tr>{nl}    <tr>{nl}      <td width={q}264{q} height={q}12{q} align={q}center{q}>{nl}      <p align={q}right{q}>Aportes (a):</td>{nl}      <td width={q}79{q} height={q}12{q} align={q}center{q}>{nl}      <p align={q}right{q}><span lang={q}es{q}>$</span></td>{nl}      <td width={q}173{q} height={q}12{q} align={q}center{q}>{nl}      <p align={q}right{q}><span lang={q}es{q}>{aportes1}</span></td>{nl}    </tr>{nl}    <tr>{nl}      <td width={q}264{q} height={q}14{q} align={q}center{q}>{nl}      <p align={q}right{q}>Aportes (<span lang={q}es{q}>b</span>):</td>{nl}<td width={q}79{q} height={q}14{q} align={q}center{q}>{nl}      <p align={q}right{q}><span lang={q}es{q}>$</span></td>{nl}      <td width={q}173{q} height={q}14{q} align={q}center{q}>{nl}      <p align={q}right{q}><span lang={q}es{q}>{aportes2}</span></td>{nl}    </tr>{nl}    <tr>{nl}      <td width={q}264{q} height={q}10{q} align={q}center{q}>{nl}      <p align={q}right{q}><span lang={q}es{q}>Reposición:</span></td>{nl}      <td width={q}79{q} height={q}10{q} align={q}center{q}>{nl}      <p align={q}right{q}><span lang={q}es{q}>$</span></td>{nl}      <td width={q}173{q} height={q}10{q} align={q}center{q}>{nl}      <p align={q}right{q}><span lang={q}es{q}>{reposicion}</span></td>{nl}    </tr>{nl}    <tr>{nl}      <td width={q}264{q} height={q}11{q} align={q}center{q}>{nl}      <p align={q}right{q}><span lang={q}es{q}>Anotación:</span></td>{nl}      <td width={q}79{q} height={q}11{q} align={q}center{q}>{nl}      <p align={q}right{q}><span lang={q}es{q}>$</span></td>{nl}      <td width={q}173{q} height={q}11{q} align={q}center{q}>{nl}      <p align={q}right{q}><span lang={q}es{q}>{anotacion}</span></td>{nl}    </tr>{nl}    <tr>{nl}      <td width={q}264{q} height={q}9{q} align={q}center{q}>{nl}      <p align={q}right{q}><span lang={q}es{q}>Gasto operativo:</span></td>{nl}      <td width={q}79{q} height={q}9{q} align={q}center{q}>{nl}      <p align={q}right{q}><span lang={q}es{q}>$</span></td>{nl}      <td width={q}173{q} height={q}9{q} align={q}center{q}>{nl}      <p align={q}right{q}><span lang={q}es{q}>{goperativo}</span></td>{nl}    </tr>{nl}"""
    if otros1 != "0,00":
        s += f"""    <tr>{nl}      <td width={q}264{q} height={q}10{q} align={q}center{q}>{nl}      <p align={q}right{q}><span lang={q}es{q}>{notros1}</span></td>{nl}      <td width={q}79{q} height={q}10{q} align={q}center{q}>{nl}      <p align={q}right{q}><span lang={q}es{q}>$</span></td>{nl}      <td width={q}173{q} height={q}10{q} align={q}center{q}>{nl}      <p align={q}right{q}><span lang={q}es{q}>{otros1}</span></td>{nl}    </tr>"""
    if otros2 != "0,00":
        s += f"""    <tr>{nl}      <td width={q}264{q} height={q}10{q} align={q}center{q}>{nl}      <p align={q}right{q}><span lang={q}es{q}>{notros2}</span></td>{nl}      <td width={q}79{q} height={q}10{q} align={q}center{q}>{nl}      <p align={q}right{q}><span lang={q}es{q}>$</span></td>{nl}      <td width={q}173{q} height={q}10{q} align={q}center{q}>{nl}      <p align={q}right{q}><span lang={q}es{q}>{otros2}</span></td>{nl}    </tr>"""
    if otros3 != "0,00":
        s += f"""    <tr>{nl}      <td width={q}264{q} height={q}10{q} align={q}center{q}>{nl}      <p align={q}right{q}><span lang={q}es{q}>{notros3}</span></td>{nl}      <td width={q}79{q} height={q}10{q} align={q}center{q}>{nl}      <p align={q}right{q}><span lang={q}es{q}>$</span></td>{nl}      <td width={q}173{q} height={q}10{q} align={q}center{q}>{nl}      <p align={q}right{q}><span lang={q}es{q}>{otros3}</span></td>{nl}    </tr>"""
    s += f"""    <tr>{nl}      <td width={q}264{q} height={q}8{q} align={q}center{q}>{nl}      </td>{nl}      <td width={q}79{q} height={q}8{q} align={q}center{q}>{nl}      </td>{nl}      <td width={q}173{q} height={q}8{q} align={q}center{q}>{nl}      </td>{nl}    </tr>{nl}    <tr>{nl}      <td width={q}264{q} height={q}16{q} align={q}center{q}>{nl}      <p align={q}right{q}><span lang={q}es{q}>Total:</span></td>{nl}      <td width={q}79{q} height={q}16{q} align={q}center{q}>{nl}      <p align={q}right{q}><span lang={q}es{q}>$</span></td>{nl}      <td width={q}173{q} height={q}16{q} align={q}center{q}>{nl}      <p align={q}right{q}><span lang={q}es{q}>{total}</span></td>{nl}    </tr>{nl}  </table>{nl}  <p>&nbsp;</p>{nl}  <p>&nbsp;</p>{nl}  <p>&nbsp;</p>{nl}  <p>&nbsp;</p>{nl}  <p>&nbsp;</p>{nl}  <p>&nbsp;</p>{nl}  </center>{nl}</div>{nl}{nl}</body>{nl}{nl}</html>"""
    return s


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
    q = '"'
    nl = "\n"
    s = f"""<html>{nl}{nl}<body>{nl}{nl}<p align={q}center{q}><font size={q}5{q}>{escribania}</font></p>{nl}<p align={q}center{q}><font size={q}4{q}>{direccion}</font></p>{nl}<p align={q}center{q}><font size={q}4{q}>{telefono}</font></p>{nl}<p align={q}center{q}><font size={q}4{q}>Presupuesto - Donación</font></p>{nl}<p align={q}center{q}>{partes}</p>{nl}<p align={q}center{q}>&nbsp;</p>{nl}<div align={q}center{q} style={q}width: 383; height: 209{q}>{nl}  <center>{nl}  <table border={q}1{q} cellpadding={q}0{q} cellspacing={q}0{q} style={q}border-collapse: collapse{q} bordercolor={q}#FFFFFF{q} width={q}256{q} height={q}1{q} id={q}AutoNumber1{q} align={q}right{q}>{nl}    <tr>{nl}      <td width={q}264{q} height={q}13{q} align={q}center{q}>{nl}      <p align={q}right{q}>Valor económico:</td>{nl}      <td width={q}79{q} height={q}13{q} align={q}center{q}>{nl}      <p align={q}right{q}><span lang={q}es{q}>$</span></td>{nl}      <td width={q}173{q} height={q}13{q} align={q}center{q}>{nl}      <p align={q}right{q}><span lang={q}es{q}>{v_economico}</span></td>{nl}    </tr>{nl}    <tr>{nl}      <td width={q}264{q} height={q}14{q} align={q}center{q}>{nl}      <p align={q}right{q}>Arancel:</td>{nl}      <td width={q}79{q} height={q}14{q} align={q}center{q}>{nl}      <p align={q}right{q}><span lang={q}es{q}>$</span></td>{nl}      <td width={q}173{q} height={q}14{q} align={q}center{q}>{nl}      <p align={q}right{q}><span lang={q}es{q}>{arancel}</span></td>{nl}    </tr>{nl}    <tr>{nl}      <td width={q}264{q} height={q}17{q} align={q}center{q}>{nl}      <p align={q}right{q}>Certificados:</td>{nl}      <td width={q}79{q} height={q}17{q} align={q}center{q}>{nl}      <p align={q}right{q}><span lang={q}es{q}>$</span></td>{nl}      <td width={q}173{q} height={q}17{q} align={q}center{q}>{nl}      <p align={q}right{q}><span lang={q}es{q}>{certificados}</span></td>{nl}    </tr>{nl}    <tr>{nl}      <td width={q}264{q} height={q}12{q} align={q}center{q}>{nl}      <p align={q}right{q}>Aportes (a):</td>{nl}      <td width={q}79{q} height={q}12{q} align={q}center{q}>{nl}      <p align={q}right{q}><span lang={q}es{q}>$</span></td>{nl}      <td width={q}173{q} height={q}12{q} align={q}center{q}>{nl}      <p align={q}right{q}><span lang={q}es{q}>{aportes1}</span></td>{nl}    </tr>{nl}    <tr>{nl}      <td width={q}264{q} height={q}14{q} align={q}center{q}>{nl}      <p align={q}right{q}>Aportes (<span lang={q}es{q}>b</span>):</td>{nl}<td width={q}79{q} height={q}14{q} align={q}center{q}>{nl}      <p align={q}right{q}><span lang={q}es{q}>$</span></td>{nl}      <td width={q}173{q} height={q}14{q} align={q}center{q}>{nl}      <p align={q}right{q}><span lang={q}es{q}>{aportes2}</span></td>{nl}    </tr>{nl}    <tr>{nl}      <td width={q}264{q} height={q}11{q} align={q}center{q}>{nl}      <p align={q}right{q}><span lang={q}es{q}>Anotación:</span></td>{nl}      <td width={q}79{q} height={q}11{q} align={q}center{q}>{nl}      <p align={q}right{q}><span lang={q}es{q}>$</span></td>{nl}      <td width={q}173{q} height={q}11{q} align={q}center{q}>{nl}      <p align={q}right{q}><span lang={q}es{q}>{anotacion}</span></td>{nl}    </tr>{nl}    <tr>{nl}      <td width={q}264{q} height={q}9{q} align={q}center{q}>{nl}      <p align={q}right{q}><span lang={q}es{q}>Gasto operativo:</span></td>{nl}      <td width={q}79{q} height={q}9{q} align={q}center{q}>{nl}      <p align={q}right{q}><span lang={q}es{q}>$</span></td>{nl}      <td width={q}173{q} height={q}9{q} align={q}center{q}>{nl}      <p align={q}right{q}><span lang={q}es{q}>{goperativo}</span></td>{nl}    </tr>{nl}"""
    if otros1 != "0,00":
        s += f"""    <tr>{nl}      <td width={q}264{q} height={q}10{q} align={q}center{q}>{nl}      <p align={q}right{q}><span lang={q}es{q}>{notros1}</span></td>{nl}      <td width={q}79{q} height={q}10{q} align={q}center{q}>{nl}      <p align={q}right{q}><span lang={q}es{q}>$</span></td>{nl}      <td width={q}173{q} height={q}10{q} align={q}center{q}>{nl}      <p align={q}right{q}><span lang={q}es{q}>{otros1}</span></td>{nl}    </tr>"""
    if otros2 != "0,00":
        s += f"""    <tr>{nl}      <td width={q}264{q} height={q}10{q} align={q}center{q}>{nl}      <p align={q}right{q}><span lang={q}es{q}>{notros2}</span></td>{nl}      <td width={q}79{q} height={q}10{q} align={q}center{q}>{nl}      <p align={q}right{q}><span lang={q}es{q}>$</span></td>{nl}      <td width={q}173{q} height={q}10{q} align={q}center{q}>{nl}      <p align={q}right{q}><span lang={q}es{q}>{otros2}</span></td>{nl}    </tr>"""
    if otros3 != "0,00":
        s += f"""    <tr>{nl}      <td width={q}264{q} height={q}10{q} align={q}center{q}>{nl}      <p align={q}right{q}><span lang={q}es{q}>{notros3}</span></td>{nl}      <td width={q}79{q} height={q}10{q} align={q}center{q}>{nl}      <p align={q}right{q}><span lang={q}es{q}>$</span></td>{nl}      <td width={q}173{q} height={q}10{q} align={q}center{q}>{nl}      <p align={q}right{q}><span lang={q}es{q}>{otros3}</span></td>{nl}    </tr>"""
    s += f"""    <tr>{nl}      <td width={q}264{q} height={q}8{q} align={q}center{q}>{nl}      </td>{nl}      <td width={q}79{q} height={q}8{q} align={q}center{q}>{nl}      </td>{nl}      <td width={q}173{q} height={q}8{q} align={q}center{q}>{nl}      </td>{nl}    </tr>{nl}    <tr>{nl}      <td width={q}264{q} height={q}16{q} align={q}center{q}>{nl}      <p align={q}right{q}><span lang={q}es{q}>Total:</span></td>{nl}      <td width={q}79{q} height={q}16{q} align={q}center{q}>{nl}      <p align={q}right{q}><span lang={q}es{q}>$</span></td>{nl}      <td width={q}173{q} height={q}16{q} align={q}center{q}>{nl}      <p align={q}right{q}><span lang={q}es{q}>{total}</span></td>{nl}    </tr>{nl}  </table>{nl}  <p>&nbsp;</p>{nl}  <p>&nbsp;</p>{nl}  <p>&nbsp;</p>{nl}  <p>&nbsp;</p>{nl}  <p>&nbsp;</p>{nl}  <p>&nbsp;</p>{nl}  </center>{nl}</div>{nl}{nl}</body>{nl}{nl}</html>"""
    return s
