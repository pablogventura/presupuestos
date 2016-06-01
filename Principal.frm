VERSION 5.00
Begin VB.Form Principal 
   BorderStyle     =   1  'Fixed Single
   Caption         =   "Presupuestos"
   ClientHeight    =   1095
   ClientLeft      =   45
   ClientTop       =   330
   ClientWidth     =   2655
   Icon            =   "Principal.frx":0000
   LinkTopic       =   "Form1"
   MaxButton       =   0   'False
   MinButton       =   0   'False
   ScaleHeight     =   1095
   ScaleWidth      =   2655
   StartUpPosition =   2  'CenterScreen
   Begin VB.CommandButton Command5 
      Caption         =   "&Salir"
      Height          =   375
      Left            =   1800
      TabIndex        =   2
      Top             =   720
      Width           =   855
   End
   Begin VB.CommandButton Command4 
      Caption         =   "&Configuración"
      Height          =   375
      Left            =   0
      TabIndex        =   1
      Top             =   720
      Width           =   1335
   End
   Begin VB.Frame Frame1 
      Caption         =   "&Operación:"
      Height          =   615
      Left            =   0
      TabIndex        =   0
      Top             =   0
      Width           =   2655
      Begin VB.ComboBox cbooperacion 
         Height          =   315
         ItemData        =   "Principal.frx":0CCA
         Left            =   120
         List            =   "Principal.frx":0CDA
         Sorted          =   -1  'True
         Style           =   2  'Dropdown List
         TabIndex        =   3
         Top             =   240
         Width           =   2415
      End
   End
End
Attribute VB_Name = "Principal"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False

Private Sub cbooperacion_Click()
Select Case cbooperacion.Text
Case "Donación"
Donacion.Show
Case "Venta"
Venta.Show
Case "Cesión de derechos onerosa"
Cesiond.Show
Case "Partición o Adjudicación"
ParticAdj.Show
End Select
Principal.Hide
End Sub

Private Sub Command4_Click()
Conf.Show
End Sub

Private Sub Command5_Click()
End
End Sub

Private Sub Form_Unload(Cancel As Integer)
End
End Sub
