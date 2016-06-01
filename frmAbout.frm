VERSION 5.00
Begin VB.Form frmAbout 
   BorderStyle     =   3  'Fixed Dialog
   Caption         =   "Acerca de MiApl"
   ClientHeight    =   1875
   ClientLeft      =   2340
   ClientTop       =   1935
   ClientWidth     =   3405
   ClipControls    =   0   'False
   Icon            =   "frmAbout.frx":0000
   LinkTopic       =   "Form2"
   MaxButton       =   0   'False
   MinButton       =   0   'False
   ScaleHeight     =   1294.158
   ScaleMode       =   0  'User
   ScaleWidth      =   3197.471
   ShowInTaskbar   =   0   'False
   StartUpPosition =   2  'CenterScreen
   Begin VB.PictureBox picIcon 
      AutoSize        =   -1  'True
      ClipControls    =   0   'False
      Height          =   540
      Left            =   240
      Picture         =   "frmAbout.frx":000C
      ScaleHeight     =   337.12
      ScaleMode       =   0  'User
      ScaleWidth      =   337.12
      TabIndex        =   1
      Top             =   240
      Width           =   540
   End
   Begin VB.CommandButton cmdOK 
      Cancel          =   -1  'True
      Caption         =   "Aceptar"
      Default         =   -1  'True
      Height          =   345
      Left            =   2160
      TabIndex        =   0
      Top             =   1440
      Width           =   1020
   End
   Begin VB.Label Label2 
      Caption         =   "pablogventura@gmail.com"
      BeginProperty Font 
         Name            =   "MS Sans Serif"
         Size            =   8.25
         Charset         =   0
         Weight          =   400
         Underline       =   -1  'True
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      ForeColor       =   &H00FF0000&
      Height          =   255
      Left            =   930
      MouseIcon       =   "frmAbout.frx":0316
      MousePointer    =   99  'Custom
      TabIndex        =   6
      Top             =   960
      Width           =   2055
   End
   Begin VB.Label Label1 
      Caption         =   "Contacto:"
      Height          =   255
      Left            =   120
      TabIndex        =   5
      Top             =   960
      Width           =   975
   End
   Begin VB.Label lblTitle 
      Caption         =   "Título de la aplicación"
      ForeColor       =   &H00000000&
      Height          =   480
      Left            =   1365
      TabIndex        =   3
      Top             =   195
      Width           =   1770
   End
   Begin VB.Label lblVersion 
      Caption         =   "Versión"
      Height          =   225
      Left            =   1365
      TabIndex        =   4
      Top             =   675
      Width           =   1725
   End
   Begin VB.Label lblDisclaimer 
      Caption         =   "© Pablo Ventura 2003-2011"
      ForeColor       =   &H00000000&
      Height          =   180
      Left            =   75
      TabIndex        =   2
      Top             =   1515
      Width           =   2310
   End
End
Attribute VB_Name = "frmAbout"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False

Private Sub cmdOK_Click()
  Unload Me
End Sub

Private Sub Form_Load()
'FAS
    Me.Icon = Nothing
    Me.Caption = "Acerca de " & App.Title
    lblVersion.Caption = "Versión " & App.Major & "." & App.Minor & "." & App.Revision
    lblTitle.Caption = App.Title
    picIcon.Picture = Principal.Icon
End Sub

Private Sub Label2_Click()
Shell "c:\archivos de programa\Internet Explorer\iexplore.exe mailto:pablogventura@gmail.com", vbNormalFocus
End Sub
