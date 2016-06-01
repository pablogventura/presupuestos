Attribute VB_Name = "Impresion"
Dim linea As String
Public Sub Dibujar()
linea = GetSetting("Presupuestos", "Impresion", "MargenSuperior", "4000")
Escribir "Escriban" & IIf(Venta.bajararancel.BackColor = vbRed, "ì", "í") & "a " & GetSetting("Presupuestos", "Escribania", "Nombre", "Ventura"), "Times New Roman", 18, "centro", linea
linea = linea + 400
Escribir GetSetting("Presupuestos", "Escribania", "Direccion", "Corrientes 5 - 4º " & Chr(34) & "A" & Chr(34)), "Times New Roman", 12, "centro", linea
linea = linea + 500
Escribir GetSetting("Presupuestos", "Escribania", "Telefonoemail", "Te: 4255715 - e-mail: gabventura@arnet.com.ar"), "Times New Roman", 12, "centro", linea
linea = linea + 700
Escribir "Presupuesto - Escritura de Venta", "Times New Roman", 16, "centro", linea
If Venta.partes = "" Then
linea = linea + 900
Else
Escribir Venta.partes, "Times New Roman", 14, "centro", 6000
linea = linea + 1400
End If
Escribir "Valor económico:", "Times New Roman", 12, "tercio", linea, 3
Escribir "$", "Times New Roman", 12, "centro", linea, 3
Escribir Venta.VEconomico, "Times New Roman", 12, "terciod", linea, 3
linea = linea + 600
Escribir "Arancel:", "Times New Roman", 12, "tercio", linea, 3
Escribir "$", "Times New Roman", 12, "centro", linea, 3
Escribir Venta.arAncel, "Times New Roman", 12, "terciod", linea, 3
linea = linea + 600
Escribir "Certificados:", "Times New Roman", 12, "tercio", linea, 3
Escribir "$", "Times New Roman", 12, "centro", linea, 3
Escribir Venta.certificado, "Times New Roman", 12, "terciod", linea, 3
linea = linea + 600
Escribir "Aportes (a):", "Times New Roman", 12, "tercio", linea, 3
Escribir "$", "Times New Roman", 12, "centro", linea, 3
Escribir Venta.aportes1, "Times New Roman", 12, "terciod", linea, 3
linea = linea + 600
Escribir "Aportes (b):", "Times New Roman", 12, "tercio", linea, 3
Escribir "$", "Times New Roman", 12, "centro", linea, 3
Escribir Venta.aportes2, "Times New Roman", 12, "terciod", linea, 3
linea = linea + 600
Escribir "Reposición:", "Times New Roman", 12, "tercio", linea, 3
Escribir "$", "Times New Roman", 12, "centro", linea, 3
Escribir Venta.reposicion, "Times New Roman", 12, "terciod", linea, 3
linea = linea + 600
Escribir "Anotación:", "Times New Roman", 12, "tercio", linea, 3
Escribir "$", "Times New Roman", 12, "centro", linea, 3
Escribir Venta.anotacion, "Times New Roman", 12, "terciod", linea, 3
linea = linea + 600
Escribir "Gasto operativo:", "Times New Roman", 12, "tercio", linea, 3
Escribir "$", "Times New Roman", 12, "centro", linea, 3
Escribir Venta.goperativo, "Times New Roman", 12, "terciod", linea, 3
linea = linea + 600
Escribir "Protocolo Ley 9343:", "Times New Roman", 12, "tercio", linea, 3
Escribir "$", "Times New Roman", 12, "centro", linea, 3
Escribir Venta.ProtoLey, "Times New Roman", 12, "terciod", linea, 3
If Venta.otros1 <> 0 Then
linea = linea + 600
Escribir Venta.notros1, "Times New Roman", 12, "tercio", linea, 3
Escribir "$", "Times New Roman", 12, "centro", linea, 3
Escribir Venta.otros1, "Times New Roman", 12, "terciod", linea, 3
End If
If Venta.otros2 <> 0 Then
linea = linea + 600
Escribir Venta.notros2, "Times New Roman", 12, "tercio", linea, 3
Escribir "$", "Times New Roman", 12, "centro", linea, 3
Escribir Venta.otros2, "Times New Roman", 12, "terciod", linea, 3
End If
If Venta.otros3 <> 0 Then
linea = linea + 600
Escribir Venta.notros3, "Times New Roman", 12, "tercio", linea, 3
Escribir "$", "Times New Roman", 12, "centro", linea, 3
Escribir Venta.otros3, "Times New Roman", 12, "terciod", linea, 3
End If
linea = linea + 600
Escribir "Total:", "Times New Roman", 12, "tercio", linea, 3
Escribir "$", "Times New Roman", 12, "centro", linea, 3
Escribir Venta.total, "Times New Roman", 12, "terciod", linea, 3
Printer.EndDoc

End Sub


Public Sub Escribir(texto As String, fuente As String, tamano As Single, posx As String, posy As String, Optional posrelativa As Integer = 2)
Printer.Font = fuente
Printer.FontSize = tamano
Select Case posx
Case "centro"
Printer.CurrentX = Printer.Width / 2
Case "tercio"
Printer.CurrentX = Printer.Width / 3
Case "terciod"
Printer.CurrentX = (Printer.Width / 3) * 2
Case "cuarto"
Printer.CurrentX = Printer.Width / 4
Case Else
Printer.CurrentX = posx
End Select
Select Case posrelativa
Case 2
Printer.CurrentX = Printer.CurrentX - (Printer.TextWidth(texto) / 2)
Case 1
Printer.CurrentX = Printer.CurrentX + Printer.TextWidth(texto)
Case 3
Printer.CurrentX = Printer.CurrentX - Printer.TextWidth(texto)
End Select
Printer.CurrentY = posy
Printer.Print texto
End Sub

Public Sub DibujarDonacion()
linea = GetSetting("Presupuestos", "Impresion", "MargenSuperior", "4000")
Escribir "Escriban" & IIf(Donacion.bajararancel.BackColor = vbRed, "ì", "í") & "a " & GetSetting("Presupuestos", "Escribania", "Nombre", "Ventura"), "Times New Roman", 18, "centro", linea
linea = linea + 400
Escribir GetSetting("Presupuestos", "Escribania", "Direccion", "Corrientes 5 - 4º " & Chr(34) & "A" & Chr(34)), "Times New Roman", 12, "centro", linea
linea = linea + 500
Escribir GetSetting("Presupuestos", "Escribania", "Telefonoemail", "Te: 4255715 - e-mail: gabventura@arnet.com.ar"), "Times New Roman", 12, "centro", linea
linea = linea + 700
Escribir "Presupuesto - Donación", "Times New Roman", 16, "centro", linea
If Donacion.partes = "" Then
linea = linea + 900
Else
Escribir Donacion.partes, "Times New Roman", 14, "centro", 6000
linea = linea + 1400
End If
Escribir "Valor económico:", "Times New Roman", 12, "tercio", linea, 3
Escribir "$", "Times New Roman", 12, "centro", linea, 3
Escribir Donacion.VEconomico, "Times New Roman", 12, "terciod", linea, 3
linea = linea + 600
Escribir "Arancel:", "Times New Roman", 12, "tercio", linea, 3
Escribir "$", "Times New Roman", 12, "centro", linea, 3
Escribir Donacion.arAncel, "Times New Roman", 12, "terciod", linea, 3
linea = linea + 600
Escribir "Certificados:", "Times New Roman", 12, "tercio", linea, 3
Escribir "$", "Times New Roman", 12, "centro", linea, 3
Escribir Donacion.certificado, "Times New Roman", 12, "terciod", linea, 3
linea = linea + 600
Escribir "Aportes (a):", "Times New Roman", 12, "tercio", linea, 3
Escribir "$", "Times New Roman", 12, "centro", linea, 3
Escribir Donacion.aportes1, "Times New Roman", 12, "terciod", linea, 3
linea = linea + 600
Escribir "Aportes (b):", "Times New Roman", 12, "tercio", linea, 3
Escribir "$", "Times New Roman", 12, "centro", linea, 3
Escribir Donacion.aportes2, "Times New Roman", 12, "terciod", linea, 3
linea = linea + 600
Escribir "Anotación:", "Times New Roman", 12, "tercio", linea, 3
Escribir "$", "Times New Roman", 12, "centro", linea, 3
Escribir Donacion.anotacion, "Times New Roman", 12, "terciod", linea, 3
linea = linea + 600
Escribir "Gasto operativo:", "Times New Roman", 12, "tercio", linea, 3
Escribir "$", "Times New Roman", 12, "centro", linea, 3
Escribir Donacion.goperativo, "Times New Roman", 12, "terciod", linea, 3
linea = linea + 600
Escribir "Protocolos Ley 9343:", "Times New Roman", 12, "tercio", linea, 3
Escribir "$", "Times New Roman", 12, "centro", linea, 3
Escribir Donacion.ProtoLey, "Times New Roman", 12, "terciod", linea, 3
If Donacion.otros1 <> 0 Then
linea = linea + 600
Escribir Donacion.notros1, "Times New Roman", 12, "tercio", linea, 3
Escribir "$", "Times New Roman", 12, "centro", linea, 3
Escribir Donacion.otros1, "Times New Roman", 12, "terciod", linea, 3
End If
If Donacion.otros2 <> 0 Then
linea = linea + 600
Escribir Donacion.notros2, "Times New Roman", 12, "tercio", linea, 3
Escribir "$", "Times New Roman", 12, "centro", linea, 3
Escribir Donacion.otros2, "Times New Roman", 12, "terciod", linea, 3
End If
If Donacion.otros3 <> 0 Then
linea = linea + 600
Escribir Donacion.notros3, "Times New Roman", 12, "tercio", linea, 3
Escribir "$", "Times New Roman", 12, "centro", linea, 3
Escribir Donacion.otros3, "Times New Roman", 12, "terciod", linea, 3
End If
linea = linea + 600
Escribir "Total:", "Times New Roman", 12, "tercio", linea, 3
Escribir "$", "Times New Roman", 12, "centro", linea, 3
Escribir Donacion.total, "Times New Roman", 12, "terciod", linea, 3
Printer.EndDoc

End Sub

Public Sub DibujarCesion()
linea = GetSetting("Presupuestos", "Impresion", "MargenSuperior", "4000")
Escribir "Escriban" & IIf(Cesiond.bajararancel.BackColor = vbRed, "ì", "í") & "a " & GetSetting("Presupuestos", "Escribania", "Nombre", "Ventura"), "Times New Roman", 18, "centro", linea
linea = linea + 400
Escribir GetSetting("Presupuestos", "Escribania", "Direccion", "Corrientes 5 - 4º " & Chr(34) & "A" & Chr(34)), "Times New Roman", 12, "centro", linea
linea = linea + 500
Escribir GetSetting("Presupuestos", "Escribania", "Telefonoemail", "Te: 4255715 - e-mail: gabventura@arnet.com.ar"), "Times New Roman", 12, "centro", linea
linea = linea + 700
Escribir "Presupuesto - Escritura de Cesión de Derechos Onerosa", "Times New Roman", 16, "centro", linea
If Cesiond.partes = "" Then
linea = linea + 900
Else
Escribir Cesiond.partes, "Times New Roman", 14, "centro", 6000
linea = linea + 1400
End If
Escribir "Valor económico:", "Times New Roman", 12, "tercio", linea, 3
Escribir "$", "Times New Roman", 12, "centro", linea, 3
Escribir Cesiond.VEconomico, "Times New Roman", 12, "terciod", linea, 3
linea = linea + 600
Escribir "Arancel:", "Times New Roman", 12, "tercio", linea, 3
Escribir "$", "Times New Roman", 12, "centro", linea, 3
Escribir Cesiond.arAncel, "Times New Roman", 12, "terciod", linea, 3
linea = linea + 600
Escribir "Certificados:", "Times New Roman", 12, "tercio", linea, 3
Escribir "$", "Times New Roman", 12, "centro", linea, 3
Escribir Cesiond.certificado, "Times New Roman", 12, "terciod", linea, 3
linea = linea + 600
Escribir "Aportes (a):", "Times New Roman", 12, "tercio", linea, 3
Escribir "$", "Times New Roman", 12, "centro", linea, 3
Escribir Cesiond.aportes1, "Times New Roman", 12, "terciod", linea, 3
linea = linea + 600
Escribir "Aportes (b):", "Times New Roman", 12, "tercio", linea, 3
Escribir "$", "Times New Roman", 12, "centro", linea, 3
Escribir Cesiond.aportes2, "Times New Roman", 12, "terciod", linea, 3
linea = linea + 600
Escribir "Reposición:", "Times New Roman", 12, "tercio", linea, 3
Escribir "$", "Times New Roman", 12, "centro", linea, 3
Escribir Cesiond.reposicion, "Times New Roman", 12, "terciod", linea, 3
linea = linea + 600
Escribir "Anotación:", "Times New Roman", 12, "tercio", linea, 3
Escribir "$", "Times New Roman", 12, "centro", linea, 3
Escribir Cesiond.anotacion, "Times New Roman", 12, "terciod", linea, 3
linea = linea + 600
Escribir "Gasto operativo:", "Times New Roman", 12, "tercio", linea, 3
Escribir "$", "Times New Roman", 12, "centro", linea, 3
Escribir Cesiond.goperativo, "Times New Roman", 12, "terciod", linea, 3
linea = linea + 600
Escribir "Protocolo Ley 9343:", "Times New Roman", 12, "tercio", linea, 3
Escribir "$", "Times New Roman", 12, "centro", linea, 3
Escribir Cesiond.ProtoLey, "Times New Roman", 12, "terciod", linea, 3
If Cesiond.otros1 <> 0 Then
linea = linea + 600
Escribir Cesiond.notros1, "Times New Roman", 12, "tercio", linea, 3
Escribir "$", "Times New Roman", 12, "centro", linea, 3
Escribir Cesiond.otros1, "Times New Roman", 12, "terciod", linea, 3
End If
If Cesiond.otros2 <> 0 Then
linea = linea + 600
Escribir Cesiond.notros2, "Times New Roman", 12, "tercio", linea, 3
Escribir "$", "Times New Roman", 12, "centro", linea, 3
Escribir Cesiond.otros2, "Times New Roman", 12, "terciod", linea, 3
End If
If Cesiond.otros3 <> 0 Then
linea = linea + 600
Escribir Cesiond.notros3, "Times New Roman", 12, "tercio", linea, 3
Escribir "$", "Times New Roman", 12, "centro", linea, 3
Escribir Cesiond.otros3, "Times New Roman", 12, "terciod", linea, 3
End If
linea = linea + 600
Escribir "Total:", "Times New Roman", 12, "tercio", linea, 3
Escribir "$", "Times New Roman", 12, "centro", linea, 3
Escribir Cesiond.total, "Times New Roman", 12, "terciod", linea, 3
Printer.EndDoc
End Sub
Public Sub DibujarParticion()
linea = GetSetting("Presupuestos", "Impresion", "MargenSuperior", "4000")
Escribir "Escriban" & IIf(ParticAdj.bajararancel.BackColor = vbRed, "ì", "í") & "a " & GetSetting("Presupuestos", "Escribania", "Nombre", "Ventura"), "Times New Roman", 18, "centro", linea
linea = linea + 400
Escribir GetSetting("Presupuestos", "Escribania", "Direccion", "Corrientes 5 - 4º " & Chr(34) & "A" & Chr(34)), "Times New Roman", 12, "centro", linea
linea = linea + 500
Escribir GetSetting("Presupuestos", "Escribania", "Telefonoemail", "Te: 4255715 - e-mail: gabventura@arnet.com.ar"), "Times New Roman", 12, "centro", linea
linea = linea + 700
Escribir "Presupuesto - Partición o Adjudicación", "Times New Roman", 16, "centro", linea
If ParticAdj.partes = "" Then
linea = linea + 900
Else
Escribir ParticAdj.partes, "Times New Roman", 14, "centro", 6000
linea = linea + 1400
End If
Escribir "Valor económico:", "Times New Roman", 12, "tercio", linea, 3
Escribir "$", "Times New Roman", 12, "centro", linea, 3
Escribir ParticAdj.VEconomico, "Times New Roman", 12, "terciod", linea, 3
linea = linea + 600
Escribir "Arancel:", "Times New Roman", 12, "tercio", linea, 3
Escribir "$", "Times New Roman", 12, "centro", linea, 3
Escribir ParticAdj.arAncel, "Times New Roman", 12, "terciod", linea, 3
linea = linea + 600
Escribir "Certificados:", "Times New Roman", 12, "tercio", linea, 3
Escribir "$", "Times New Roman", 12, "centro", linea, 3
Escribir ParticAdj.certificado, "Times New Roman", 12, "terciod", linea, 3
linea = linea + 600
Escribir "Aportes (a):", "Times New Roman", 12, "tercio", linea, 3
Escribir "$", "Times New Roman", 12, "centro", linea, 3
Escribir ParticAdj.aportes1, "Times New Roman", 12, "terciod", linea, 3
linea = linea + 600
Escribir "Aportes (b):", "Times New Roman", 12, "tercio", linea, 3
Escribir "$", "Times New Roman", 12, "centro", linea, 3
Escribir ParticAdj.aportes2, "Times New Roman", 12, "terciod", linea, 3
linea = linea + 600
Escribir "Anotación:", "Times New Roman", 12, "tercio", linea, 3
Escribir "$", "Times New Roman", 12, "centro", linea, 3
Escribir ParticAdj.anotacion, "Times New Roman", 12, "terciod", linea, 3
linea = linea + 600
Escribir "Gasto operativo:", "Times New Roman", 12, "tercio", linea, 3
Escribir "$", "Times New Roman", 12, "centro", linea, 3
Escribir ParticAdj.goperativo, "Times New Roman", 12, "terciod", linea, 3
linea = linea + 600
Escribir "Protocolo Ley 9343:", "Times New Roman", 12, "tercio", linea, 3
Escribir "$", "Times New Roman", 12, "centro", linea, 3
Escribir ParticAdj.ProtoLey, "Times New Roman", 12, "terciod", linea, 3
If ParticAdj.otros1 <> 0 Then
linea = linea + 600
Escribir ParticAdj.notros1, "Times New Roman", 12, "tercio", linea, 3
Escribir "$", "Times New Roman", 12, "centro", linea, 3
Escribir ParticAdj.otros1, "Times New Roman", 12, "terciod", linea, 3
End If
If ParticAdj.otros2 <> 0 Then
linea = linea + 600
Escribir ParticAdj.notros2, "Times New Roman", 12, "tercio", linea, 3
Escribir "$", "Times New Roman", 12, "centro", linea, 3
Escribir ParticAdj.otros2, "Times New Roman", 12, "terciod", linea, 3
End If
If ParticAdj.otros3 <> 0 Then
linea = linea + 600
Escribir ParticAdj.notros3, "Times New Roman", 12, "tercio", linea, 3
Escribir "$", "Times New Roman", 12, "centro", linea, 3
Escribir ParticAdj.otros3, "Times New Roman", 12, "terciod", linea, 3
End If
linea = linea + 600
Escribir "Total:", "Times New Roman", 12, "tercio", linea, 3
Escribir "$", "Times New Roman", 12, "centro", linea, 3
Escribir ParticAdj.total, "Times New Roman", 12, "terciod", linea, 3
Printer.EndDoc

End Sub
