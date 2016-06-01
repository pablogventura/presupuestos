VERSION 5.00
Object = "{FE0065C0-1B7B-11CF-9D53-00AA003C9CB6}#1.1#0"; "COMCT232.OCX"
Begin VB.Form Conf 
   BorderStyle     =   3  'Fixed Dialog
   Caption         =   "Configuración de Presupuestos"
   ClientHeight    =   3135
   ClientLeft      =   45
   ClientTop       =   330
   ClientWidth     =   5535
   Icon            =   "Form2.frx":0000
   LinkTopic       =   "Form2"
   MaxButton       =   0   'False
   MinButton       =   0   'False
   ScaleHeight     =   3135
   ScaleWidth      =   5535
   ShowInTaskbar   =   0   'False
   StartUpPosition =   2  'CenterScreen
   Begin VB.CommandButton Command2 
      Cancel          =   -1  'True
      Caption         =   "&Cancelar"
      Height          =   855
      Left            =   4200
      TabIndex        =   18
      Top             =   2280
      Width           =   1335
   End
   Begin VB.CommandButton cdaceptar 
      Caption         =   "&Aceptar"
      Default         =   -1  'True
      Height          =   855
      Left            =   2760
      TabIndex        =   17
      Top             =   2280
      Width           =   1335
   End
   Begin VB.Frame Frame3 
      Caption         =   "e-mail:"
      Height          =   2055
      Left            =   2760
      TabIndex        =   10
      Top             =   120
      Width           =   2775
      Begin VB.TextBox ssmtp 
         Height          =   285
         Left            =   120
         TabIndex        =   16
         Top             =   1680
         Width           =   2535
      End
      Begin VB.TextBox nremitente 
         Height          =   285
         Left            =   120
         TabIndex        =   14
         Top             =   1080
         Width           =   2535
      End
      Begin VB.TextBox email 
         Height          =   285
         Left            =   120
         TabIndex        =   12
         Top             =   480
         Width           =   2535
      End
      Begin VB.Label Label7 
         Caption         =   "Servidor smtp:"
         Height          =   255
         Left            =   120
         TabIndex        =   15
         Top             =   1440
         Width           =   2535
      End
      Begin VB.Label Label6 
         Caption         =   "Nombre del remitente:"
         Height          =   255
         Left            =   120
         TabIndex        =   13
         Top             =   840
         Width           =   2415
      End
      Begin VB.Label Label5 
         Caption         =   "e-mail de origen:"
         Height          =   255
         Left            =   120
         TabIndex        =   11
         Top             =   240
         Width           =   2415
      End
   End
   Begin VB.Frame Frame2 
      Caption         =   "Impresión:"
      Height          =   855
      Left            =   0
      TabIndex        =   7
      Top             =   2280
      Width           =   2655
      Begin ComCtl2.UpDown UpDown1 
         Height          =   225
         Left            =   2250
         TabIndex        =   19
         Top             =   510
         Width           =   240
         _ExtentX        =   450
         _ExtentY        =   397
         _Version        =   327681
         AutoBuddy       =   -1  'True
         BuddyControl    =   "msuperior"
         BuddyDispid     =   196619
         OrigLeft        =   2280
         OrigTop         =   480
         OrigRight       =   2520
         OrigBottom      =   735
         Increment       =   500
         Max             =   100000
         SyncBuddy       =   -1  'True
         BuddyProperty   =   0
         Enabled         =   -1  'True
      End
      Begin VB.TextBox msuperior 
         Height          =   285
         Left            =   120
         TabIndex        =   9
         Top             =   480
         Width           =   2400
      End
      Begin VB.Label Label4 
         Caption         =   "Margen superior (en twips):"
         Height          =   255
         Left            =   120
         TabIndex        =   8
         Top             =   240
         Width           =   1935
      End
   End
   Begin VB.Frame Frame1 
      Caption         =   "Escribanía:"
      Height          =   2055
      Left            =   0
      TabIndex        =   0
      Top             =   120
      Width           =   2655
      Begin VB.TextBox teescribania 
         Height          =   285
         Left            =   120
         TabIndex        =   6
         Top             =   1680
         Width           =   2415
      End
      Begin VB.TextBox describania 
         Height          =   285
         Left            =   120
         TabIndex        =   4
         Top             =   1080
         Width           =   2415
      End
      Begin VB.TextBox nescribania 
         Height          =   285
         Left            =   120
         TabIndex        =   2
         Top             =   480
         Width           =   2415
      End
      Begin VB.Label Label3 
         Caption         =   "Teléfono - E-mail:"
         Height          =   255
         Left            =   120
         TabIndex        =   5
         Top             =   1440
         Width           =   2415
      End
      Begin VB.Label Label2 
         Caption         =   "Dirección:"
         Height          =   255
         Left            =   120
         TabIndex        =   3
         Top             =   840
         Width           =   2415
      End
      Begin VB.Label Label1 
         Caption         =   "Nombre:"
         Height          =   255
         Left            =   120
         TabIndex        =   1
         Top             =   240
         Width           =   2175
      End
   End
End
Attribute VB_Name = "Conf"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False

Private Sub cdAceptar_Click()
SaveSetting "Presupuestos", "Escribania", "Nombre", nescribania
SaveSetting "Presupuestos", "Escribania", "Direccion", describania
SaveSetting "Presupuestos", "Escribania", "Telefonoemail", teescribania
SaveSetting "Presupuestos", "Impresion", "MargenSuperior", msuperior
SaveSetting "Presupuestos", "email", "email", email
SaveSetting "Presupuestos", "email", "NRemitente", nremitente
SaveSetting "Presupuestos", "email", "Servidor", ssmtp
Unload Me
End Sub

Private Sub Command2_Click()
Unload Me
End Sub

Private Sub Form_Load()
Conf.Icon = Nothing
nescribania = GetSetting("Presupuestos", "Escribania", "Nombre", "Ventura")
describania = GetSetting("Presupuestos", "Escribania", "Direccion", "Corrientes 5 - 4º " & Chr(34) & "A" & Chr(34))
teescribania = GetSetting("Presupuestos", "Escribania", "Telefonoemail", "Te: 4255715 - e-mail: gabventura@arnet.com.ar")
msuperior = GetSetting("Presupuestos", "Impresion", "MargenSuperior", "4000")
email = GetSetting("Presupuestos", "email", "email", "gabventura@arnet.com.ar")
nremitente = GetSetting("Presupuestos", "email", "NRemitente", "Gabriel B. Ventura")
ssmtp = GetSetting("Presupuestos", "email", "Servidor", "smtp.arnet.com.ar")
End Sub
