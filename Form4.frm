VERSION 5.00
Object = "{F9043C88-F6F2-101A-A3C9-08002B2F49FB}#1.2#0"; "COMDLG32.OCX"
Begin VB.Form Donacion 
   BorderStyle     =   1  'Fixed Single
   Caption         =   "Donación"
   ClientHeight    =   6135
   ClientLeft      =   150
   ClientTop       =   435
   ClientWidth     =   3495
   Icon            =   "Form4.frx":0000
   LinkTopic       =   "Form1"
   MaxButton       =   0   'False
   MinButton       =   0   'False
   ScaleHeight     =   6135
   ScaleWidth      =   3495
   StartUpPosition =   2  'CenterScreen
   Begin MSComDlg.CommonDialog cd 
      Left            =   2400
      Top             =   0
      _ExtentX        =   847
      _ExtentY        =   847
      _Version        =   393216
      CancelError     =   -1  'True
   End
   Begin VB.Frame Frame4 
      Caption         =   "Partes:"
      Height          =   615
      Left            =   120
      TabIndex        =   27
      Top             =   840
      Width           =   3135
      Begin VB.TextBox partes 
         Enabled         =   0   'False
         Height          =   285
         Left            =   120
         TabIndex        =   2
         Top             =   240
         Width           =   2895
      End
   End
   Begin VB.CommandButton calcular 
      Caption         =   "Calcular"
      Default         =   -1  'True
      Height          =   495
      Left            =   2160
      TabIndex        =   1
      ToolTipText     =   "Calcular"
      Top             =   240
      Width           =   1095
   End
   Begin VB.Frame Frame1 
      Caption         =   "Valor económico:"
      Height          =   615
      Left            =   120
      TabIndex        =   17
      Top             =   120
      Width           =   1935
      Begin VB.TextBox VEconomico 
         Height          =   285
         Left            =   120
         TabIndex        =   0
         Text            =   "0,00"
         Top             =   240
         Width           =   1695
      End
   End
   Begin VB.Frame Frame2 
      Caption         =   "Presupuesto:"
      Height          =   4455
      Left            =   120
      TabIndex        =   18
      Top             =   1560
      Width           =   3255
      Begin VB.TextBox ProtoLey 
         Enabled         =   0   'False
         Height          =   285
         Left            =   1680
         TabIndex        =   28
         Text            =   "0,00"
         Top             =   2400
         Width           =   1455
      End
      Begin VB.CommandButton Command1 
         Enabled         =   0   'False
         Height          =   495
         Left            =   120
         Picture         =   "Form4.frx":0442
         Style           =   1  'Graphical
         TabIndex        =   16
         ToolTipText     =   "Imprimir"
         Top             =   3960
         Width           =   1215
      End
      Begin VB.CommandButton bajararancel 
         BackColor       =   &H00C0C0C0&
         Caption         =   "/"
         Enabled         =   0   'False
         Height          =   225
         Left            =   2880
         Style           =   1  'Graphical
         TabIndex        =   26
         Top             =   270
         Width           =   225
      End
      Begin VB.TextBox otros3 
         Enabled         =   0   'False
         Height          =   285
         Left            =   1680
         TabIndex        =   13
         Text            =   "0,00"
         Top             =   3480
         Width           =   1455
      End
      Begin VB.TextBox notros3 
         Alignment       =   1  'Right Justify
         Enabled         =   0   'False
         Height          =   285
         Left            =   120
         TabIndex        =   14
         Text            =   "Otros:"
         Top             =   3480
         Width           =   1455
      End
      Begin VB.TextBox otros2 
         Enabled         =   0   'False
         Height          =   285
         Left            =   1680
         TabIndex        =   11
         Text            =   "0,00"
         Top             =   3120
         Width           =   1455
      End
      Begin VB.TextBox notros1 
         Alignment       =   1  'Right Justify
         Enabled         =   0   'False
         Height          =   285
         Left            =   120
         TabIndex        =   10
         Text            =   "Otros:"
         Top             =   2760
         Width           =   1455
      End
      Begin VB.TextBox notros2 
         Alignment       =   1  'Right Justify
         Enabled         =   0   'False
         Height          =   285
         Left            =   120
         TabIndex        =   12
         Text            =   "Otros:"
         Top             =   3120
         Width           =   1455
      End
      Begin VB.Frame Frame3 
         Caption         =   "Total:"
         Height          =   615
         Left            =   1560
         TabIndex        =   25
         Top             =   3840
         Width           =   1575
         Begin VB.TextBox total 
            Enabled         =   0   'False
            Height          =   285
            Left            =   120
            TabIndex        =   15
            Text            =   "0,00"
            Top             =   240
            Width           =   1335
         End
      End
      Begin VB.TextBox arAncel 
         BeginProperty DataFormat 
            Type            =   0
            Format          =   "0,00"
            HaveTrueFalseNull=   0
            FirstDayOfWeek  =   0
            FirstWeekOfYear =   0
            LCID            =   11274
            SubFormatType   =   0
         EndProperty
         Enabled         =   0   'False
         Height          =   285
         Left            =   1680
         TabIndex        =   3
         Text            =   "0,00"
         Top             =   240
         Width           =   1455
      End
      Begin VB.TextBox certificado 
         Enabled         =   0   'False
         Height          =   285
         Left            =   1680
         TabIndex        =   4
         Text            =   "0,00"
         Top             =   600
         Width           =   1455
      End
      Begin VB.TextBox aportes1 
         Enabled         =   0   'False
         Height          =   285
         Left            =   1680
         TabIndex        =   5
         Text            =   "0,00"
         Top             =   960
         Width           =   1455
      End
      Begin VB.TextBox aportes2 
         Enabled         =   0   'False
         Height          =   285
         Left            =   1680
         TabIndex        =   6
         Text            =   "0,00"
         Top             =   1320
         Width           =   1455
      End
      Begin VB.TextBox anotacion 
         Enabled         =   0   'False
         Height          =   285
         Left            =   1680
         TabIndex        =   7
         Text            =   "0,00"
         Top             =   1680
         Width           =   1455
      End
      Begin VB.TextBox goperativo 
         Enabled         =   0   'False
         Height          =   285
         Left            =   1680
         TabIndex        =   8
         Text            =   "0,00"
         Top             =   2040
         Width           =   1455
      End
      Begin VB.TextBox otros1 
         Enabled         =   0   'False
         Height          =   285
         Left            =   1680
         TabIndex        =   9
         Text            =   "0,00"
         Top             =   2760
         Width           =   1455
      End
      Begin VB.Label Label6 
         Alignment       =   1  'Right Justify
         Caption         =   "Protocolos Ley 9343:"
         Height          =   255
         Left            =   120
         TabIndex        =   29
         Top             =   2400
         Width           =   1575
      End
      Begin VB.Label Label2 
         Alignment       =   1  'Right Justify
         Caption         =   "Arancel:"
         Height          =   255
         Left            =   240
         TabIndex        =   24
         Top             =   240
         Width           =   1335
      End
      Begin VB.Label Label3 
         Alignment       =   1  'Right Justify
         Caption         =   "Certificados:"
         Height          =   255
         Left            =   240
         TabIndex        =   23
         Top             =   600
         Width           =   1335
      End
      Begin VB.Label Label4 
         Alignment       =   1  'Right Justify
         Caption         =   "Aportes 1:"
         Height          =   255
         Left            =   240
         TabIndex        =   22
         Top             =   960
         Width           =   1335
      End
      Begin VB.Label Label5 
         Alignment       =   1  'Right Justify
         Caption         =   "Aportes 2:"
         Height          =   255
         Left            =   240
         TabIndex        =   21
         Top             =   1320
         Width           =   1335
      End
      Begin VB.Label Label7 
         Alignment       =   1  'Right Justify
         Caption         =   "Anotación:"
         Height          =   255
         Left            =   240
         TabIndex        =   20
         Top             =   1680
         Width           =   1335
      End
      Begin VB.Label Label8 
         Alignment       =   1  'Right Justify
         Caption         =   "Gasto operativo:"
         Height          =   255
         Left            =   240
         TabIndex        =   19
         Top             =   2040
         Width           =   1335
      End
   End
   Begin VB.Menu Archivo 
      Caption         =   "&Archivo"
      Begin VB.Menu selectopera 
         Caption         =   "Selecionar otra &operación..."
      End
      Begin VB.Menu fssfcbnfhfj 
         Caption         =   "-"
      End
      Begin VB.Menu epemail 
         Caption         =   "Enviar por e-&mail..."
      End
      Begin VB.Menu ecpw 
         Caption         =   "Exportar como &Página Web..."
      End
      Begin VB.Menu asdfsa43534 
         Caption         =   "-"
      End
      Begin VB.Menu Imprimir 
         Caption         =   "&Imprimir"
      End
      Begin VB.Menu gsdfsafd 
         Caption         =   "-"
      End
      Begin VB.Menu asdfasdf 
         Caption         =   "&Configuración..."
      End
      Begin VB.Menu sfdgsdfg546vds 
         Caption         =   "-"
      End
      Begin VB.Menu Salir 
         Caption         =   "&Salir"
      End
   End
   Begin VB.Menu edicion 
      Caption         =   "&Edición"
      Begin VB.Menu sfdasdfasfdasdf 
         Caption         =   "&Copiar resultados en HTML"
         Enabled         =   0   'False
      End
      Begin VB.Menu gsdgfs 
         Caption         =   "-"
      End
      Begin VB.Menu pveconomico 
         Caption         =   "&Pegar Valor Económico"
      End
      Begin VB.Menu sdfgsdfgdfg6t 
         Caption         =   "-"
      End
      Begin VB.Menu btodo 
         Caption         =   "&Borrar todo"
      End
   End
   Begin VB.Menu Ayuda 
      Caption         =   "A&yuda"
      Begin VB.Menu Contenido 
         Caption         =   "&Contenido"
         Enabled         =   0   'False
      End
      Begin VB.Menu asdfhgr5ghfd 
         Caption         =   "-"
      End
      Begin VB.Menu acercade 
         Caption         =   "&Acerca de.."
      End
   End
End
Attribute VB_Name = "Donacion"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Dim aplicadamitad As Boolean

Private Sub acercade_Click()
frmAbout.Show
End Sub

Private Sub anotacion_GotFocus()
anotacion.SelStart = 0
anotacion.SelLength = Len(anotacion)
End Sub

Private Sub anotacion_LostFocus()
If IsNumeric(anotacion) = False Then
anotacion = "0,00"
Else
total = SumarTodo()
anotacion = AgregaDecimales(CStr(anotacion))
End If
End Sub

Private Sub aportes1_GotFocus()
aportes1.SelStart = 0
aportes1.SelLength = Len(aportes1)
End Sub

Private Sub aportes1_LostFocus()
If IsNumeric(aportes1) = False Then
aportes1 = "0,00"
Else
total = SumarTodo()
certificado = AgregaDecimales(CStr(certificado))
End If
End Sub

Private Sub aportes2_GotFocus()
aportes2.SelStart = 0
aportes2.SelLength = Len(aportes2)
End Sub

Private Sub aportes2_LostFocus()
If IsNumeric(aportes2) = False Then
aportes2 = "0,00"
Else
total = SumarTodo()
aportes2 = AgregaDecimales(CStr(aportes2))
End If
End Sub

Private Sub arAncel_Change()
aplicadamitad = False
bajararancel.BackColor = &HC0C0C0
On Error Resume Next
If arAncel = 0 Then
bajararancel.Enabled = False
Else
bajararancel.Enabled = True
End If
End Sub

Private Sub arAncel_GotFocus()
arAncel.SelStart = 0
arAncel.SelLength = Len(arAncel)
End Sub

Private Sub arAncel_LostFocus()
If IsNumeric(arAncel) = False Then
arAncel = "0,00"
Else
total = SumarTodo()
arAncel = AgregaDecimales(CStr(arAncel))
End If
End Sub

Private Sub asdfasdf_Click()
Conf.Show
End Sub

Private Sub bajararancel_Click()
If aplicadamitad = False Then
arAncel = arAncel / 2
total = SumarTodo()
arAncel = AgregaDecimales(CStr(arAncel))
aplicadamitad = True
bajararancel.BackColor = vbRed
Else
End If
End Sub

Private Sub btodo_Click()
VEconomico = "0,00"
partes = ""
arAncel = "0,00"
certificado = "0,00"
aportes1 = "0,00"
aportes2 = "0,00"
anotacion = "0,00"
goperativo = "0,00"
otros1 = "0,00"
otros2 = "0,00"
otros3 = "0,00"
notros1 = "Otros:"
notros2 = "Otros:"
notros3 = "Otros:"
aplicadamitad = False
bajararancel.BackColor = &H8000000F
partes.Enabled = False
arAncel.Enabled = False
certificado.Enabled = False
aportes1.Enabled = False
aportes2.Enabled = False
anotacion.Enabled = False
goperativo.Enabled = False
otros1.Enabled = False
otros2.Enabled = False
otros3.Enabled = False
notros1.Enabled = False
notros2.Enabled = False
notros3.Enabled = False
Command1.Enabled = False
total.Enabled = False
End Sub

Private Sub calcular_Click()
If Not IsNumeric(VEconomico) Then
    MsgBox "El Valor economico debe ser numérico", vbCritical
    Exit Sub
End If
If Not IsNumeric(otros1) Then
MsgBox notros1 & " debe ser numérico", vbCritical
End If
If Not IsNumeric(otros2) Then
MsgBox notros2 & " debe ser numérico", vbCritical
End If
If Not IsNumeric(otros3) Then
MsgBox notros3 & " debe ser numérico", vbCritical
End If
VEconomico = AgregaDecimales(CStr(VEconomico))
arAncel = AgregaDecimales(CStr(CDbl(VEconomico) * 0.02 + 27.7))
certificado = AgregaDecimales(CStr(700))
aportes1 = AgregaDecimales(CStr(((CDbl(VEconomico) * 0.02 + 27.7) / 2) * 0.18))
aportes2 = AgregaDecimales(CStr(CDbl(VEconomico) * 0.003))
anotacion = AgregaDecimales(CStr(CDbl(0.002 * VEconomico)))
If anotacion < 30 Then
anotacion = "30,00"
End If
goperativo = AgregaDecimales(CStr(1000))
ProtoLey = AgregaDecimales(CStr(150))

total = SumarTodo()
arAncel.Enabled = True
certificado.Enabled = True
aportes1.Enabled = True
aportes2.Enabled = True
anotacion.Enabled = True
goperativo.Enabled = True
anotacion.Enabled = True
goperativo.Enabled = True
ProtoLey.Enabled = True
otros1.Enabled = True
otros2.Enabled = True
otros3.Enabled = True
notros1.Enabled = True
notros2.Enabled = True
notros3.Enabled = True
total.Enabled = True
Command1.Enabled = True
partes.Enabled = True
End Sub

Private Sub certificado_GotFocus()
certificado.SelStart = 0
certificado.SelLength = Len(certificado)
End Sub

Private Sub certificado_LostFocus()
If IsNumeric(certificado) = False Then
certificado = "0,00"
Else
total = SumarTodo()
certificado = AgregaDecimales(CStr(certificado))
End If
End Sub

Private Sub Command1_Click()
DibujarDonacion
End Sub

Private Sub ecpw_Click()

Dim pWt As String
cd.DialogTitle = "Exportar como Página Web..."
cd.Filter = "Página Web (*.htm)|*.htm"
cd.Flags = cdlOFNHideReadOnly + cdlOFNOverwritePrompt
On Error Resume Next
cd.ShowSave
If Not Err.Number = cdlCancel Then
'pWt = GenHTMLDonacion("Escribanía " & GetSetting("Presupuestos", "Escribania", "Nombre", "Ventura"), GetSetting("Presupuestos", "Escribania", "Direccion", "Corrientes 5 - 4º " & Chr(34) & "A" & Chr(34)), GetSetting("Presupuestos", "Escribania", "Telefonoemail", "Te: 4255715 - e-mail: gabventura@arnet.com.ar"), Donacion.partes, Donacion.VEconomico, Donacion.arAncel, Donacion.certificado, Donacion.aportes1, Donacion.aportes2, Donacion.anotacion, Donacion.goperativo, Donacion.total, Donacion.notros1, Donacion.otros1, Donacion.notros2, Donacion.otros2, Donacion.notros3, Donacion.otros3)
Open cd.FileName For Binary As #1
    Put 1, , pWt
Close
End If
End Sub

Private Sub epemail_Click()
Load EEmail
EEmail.lbloperacion = "Donación"
EEmail.Show
End Sub

Private Sub Form_Load()
aplicadamitad = False
End Sub

Private Sub Form_Unload(Cancel As Integer)
End
End Sub

Private Sub goperativo_GotFocus()
goperativo.SelStart = 0
goperativo.SelLength = Len(goperativo)
End Sub

Private Sub goperativo_LostFocus()
If IsNumeric(goperativo) = False Then
goperativo = "0,00"
Else
total = SumarTodo()
goperativo = AgregaDecimales(CStr(goperativo))
End If
End Sub

Private Sub Imprimir_Click()

Command1_Click
End Sub

Private Sub notros1_GotFocus()
notros1.SelStart = 0
notros1.SelLength = Len(notros1)
End Sub

Private Sub notros2_GotFocus()
notros2.SelStart = 0
notros2.SelLength = Len(notros2)
End Sub

Private Sub notros3_GotFocus()
notros3.SelStart = 0
notros3.SelLength = Len(notros3)
End Sub

Private Sub otros1_GotFocus()
otros1.SelStart = 0
otros1.SelLength = Len(otros1)
End Sub

Private Sub otros1_LostFocus()
If IsNumeric(otros1) = False Then
otros1 = "0,00"
Else
total = SumarTodo()
otros1 = AgregaDecimales(CStr(otros1))
End If
End Sub

Private Sub otros2_GotFocus()
otros2.SelStart = 0
otros2.SelLength = Len(otros2)
End Sub

Private Sub otros2_LostFocus()
If IsNumeric(otros2) = False Then
otros2 = "0,00"
Else
total = SumarTodo()
otros2 = AgregaDecimales(CStr(otros2))
End If
End Sub

Private Sub otros3_GotFocus()
otros3.SelStart = 0
otros3.SelLength = Len(otros3)
End Sub

Private Sub otros3_LostFocus()
If IsNumeric(otros3) = False Then
otros3 = "0,00"
Else
total = SumarTodo()
otros3 = AgregaDecimales(CStr(otros3))
End If
End Sub

Private Sub partes_GotFocus()
partes.SelStart = 0
partes.SelLength = Len(partes)
End Sub

Private Sub protoley_GotFocus()
ProtoLey.SelStart = 0
ProtoLey.SelLength = Len(ProtoLey)
End Sub

Private Sub protoley_LostFocus()
If IsNumeric(ProtoLey) = False Then
ProtoLey = "0,00"
Else
total = SumarTodo()
ProtoLey = AgregaDecimales(CStr(ProtoLey))
End If
End Sub

Private Sub pveconomico_Click()
VEconomico = Clipboard.GetText
End Sub

Private Sub Salir_Click()
End
End Sub

Private Sub selectopera_Click()
Principal.Show
Unload Me
End Sub

Private Sub sfdasdfasfdasdf_Click()
'Clipboard.SetText GenHTML("Escribanía " & GetSetting("Presupuestos", "Escribania", "Nombre", "Ventura"), GetSetting("Presupuestos", "Escribania", "Direccion", "Corrientes 5 - 4º " & Chr(34) & "A" & Chr(34)), GetSetting("Presupuestos", "Escribania", "Telefonoemail", "Te: 4255715 - e-mail: gabventura@arnet.com.ar"), partes, VEconomico, arAncel, certificado, aportes1, aportes2, anotacion, goperativo, total, notros1, otros1, notros2, otros2, notros3, otros3, "Donación")
End Sub

Private Sub total_GotFocus()
total.SelStart = 0
total.SelLength = Len(total)
End Sub

Private Sub VEconomico_GotFocus()
VEconomico.SelStart = 0
VEconomico.SelLength = Len(VEconomico)
End Sub

Private Function SumarTodo() As String
SumarTodo = AgregaDecimales(CStr(CDbl(arAncel) + CDbl(certificado) + CDbl(aportes1) + CDbl(aportes2) + CDbl(anotacion) + CDbl(goperativo) + CDbl(ProtoLey) + CDbl(otros1) + CDbl(otros2) + CDbl(otros3)))
End Function
