VERSION 5.00
Begin VB.Form Form1 
   Caption         =   "Form1"
   ClientHeight    =   5235
   ClientLeft      =   60
   ClientTop       =   345
   ClientWidth     =   7830
   BeginProperty Font 
      Name            =   "MS Sans Serif"
      Size            =   13.5
      Charset         =   0
      Weight          =   400
      Underline       =   0   'False
      Italic          =   0   'False
      Strikethrough   =   0   'False
   EndProperty
   LinkTopic       =   "Form1"
   ScaleHeight     =   5235
   ScaleWidth      =   7830
   StartUpPosition =   3  'Windows Default
   Begin VB.TextBox Text1 
      BeginProperty Font 
         Name            =   "MS Sans Serif"
         Size            =   8.25
         Charset         =   0
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   285
      Left            =   480
      TabIndex        =   1
      Text            =   "Text1"
      Top             =   480
      Width           =   3495
   End
   Begin VB.CommandButton Command1 
      Caption         =   "Command1"
      BeginProperty Font 
         Name            =   "MS Sans Serif"
         Size            =   8.25
         Charset         =   0
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   615
      Left            =   4680
      TabIndex        =   0
      Top             =   240
      Width           =   1575
   End
End
Attribute VB_Name = "Form1"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Dim linea As String
Private Sub Dibujar(obj As Object)
Escribir obj, "Escribanía Ventura", "Times New Roman", 18, "centro", 1000
Escribir obj, "Bv. San Juan 380 - P.B " & Chr(34) & "A" & Chr(34), "Times New Roman", 12, "centro", 1400
Escribir obj, "Te: 4255715 - e-mail: gabventura@arnet.com.ar", "Times New Roman", 12, "centro", 1600
Escribir obj, "Presupuesto - Escritura de Venta", "Times New Roman", 16, "centro", 2600
linea = 3250
Escribir obj, "Valor económico:", "Times New Roman", 12, "tercio", linea, 3
Escribir obj, "$", "Times New Roman", 12, "centro", linea, 3
Escribir obj, "123,33", "Times New Roman", 12, "terciod", linea, 3
linea = linea + 400
Escribir obj, "Arancel:", "Times New Roman", 12, "tercio", linea, 3
Escribir obj, "$", "Times New Roman", 12, "centro", linea, 3
Escribir obj, "123,33", "Times New Roman", 12, "terciod", linea, 3
linea = linea + 400
Escribir obj, "Certificados:", "Times New Roman", 12, "tercio", linea, 3
Escribir obj, "$", "Times New Roman", 12, "centro", linea, 3
Escribir obj, "123,33", "Times New Roman", 12, "terciod", linea, 3
linea = linea + 400
Escribir obj, "Aportes (a):", "Times New Roman", 12, "tercio", linea, 3
Escribir obj, "$", "Times New Roman", 12, "centro", linea, 3
Escribir obj, "123,33", "Times New Roman", 12, "terciod", linea, 3
linea = linea + 400
Escribir obj, "Aportes (b):", "Times New Roman", 12, "tercio", linea, 3
Escribir obj, "$", "Times New Roman", 12, "centro", linea, 3
Escribir obj, "123,33", "Times New Roman", 12, "terciod", linea, 3
linea = linea + 400
Escribir obj, "Reposición:", "Times New Roman", 12, "tercio", linea, 3
Escribir obj, "$", "Times New Roman", 12, "centro", linea, 3
Escribir obj, "123,33", "Times New Roman", 12, "terciod", linea, 3
linea = linea + 400
Escribir obj, "Anotación:", "Times New Roman", 12, "tercio", linea, 3
Escribir obj, "$", "Times New Roman", 12, "centro", linea, 3
Escribir obj, "123,33", "Times New Roman", 12, "terciod", linea, 3
linea = linea + 400
Escribir obj, "Gasto operativo:", "Times New Roman", 12, "tercio", linea, 3
Escribir obj, "$", "Times New Roman", 12, "centro", linea, 3
Escribir obj, "123,33", "Times New Roman", 12, "terciod", linea, 3

End Sub


Public Sub Escribir(obj As Object, texto As String, fuente As String, tamano As Single, posx As String, posy As String, Optional posrelativa As Integer = 2)

obj.Font = fuente
obj.FontSize = tamano
Select Case posx
Case "centro"
obj.CurrentX = obj.Width / 2
Case "tercio"
obj.CurrentX = obj.Width / 3
Case "terciod"
obj.CurrentX = (obj.Width / 3) * 2
Case "cuarto"
obj.CurrentX = obj.Width / 4
Case Else
obj.CurrentX = posx
End Select
Select Case posrelativa
Case 2
obj.CurrentX = obj.CurrentX - (obj.TextWidth(texto) / 2)
Case 1
obj.CurrentX = obj.CurrentX + obj.TextWidth(texto)
Case 3
obj.CurrentX = obj.CurrentX - obj.TextWidth(texto)
End Select
obj.CurrentY = posy
obj.Print texto
End Sub
