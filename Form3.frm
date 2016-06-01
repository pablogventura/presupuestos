VERSION 5.00
Object = "{831FDD16-0C5C-11D2-A9FC-0000F8754DA1}#2.0#0"; "MSCOMCTL.OCX"
Begin VB.Form Form3 
   BorderStyle     =   3  'Fixed Dialog
   Caption         =   "Enviar por e-mail"
   ClientHeight    =   4815
   ClientLeft      =   45
   ClientTop       =   330
   ClientWidth     =   5415
   LinkTopic       =   "Form3"
   MaxButton       =   0   'False
   MinButton       =   0   'False
   ScaleHeight     =   4815
   ScaleWidth      =   5415
   ShowInTaskbar   =   0   'False
   StartUpPosition =   3  'Windows Default
   Begin VB.CommandButton Command1 
      Caption         =   "Enviar"
      Height          =   375
      Left            =   0
      TabIndex        =   6
      Top             =   4440
      Width           =   1215
   End
   Begin MSComctlLib.ProgressBar ProgressBar1 
      Height          =   375
      Left            =   1320
      TabIndex        =   5
      Top             =   4440
      Width           =   4095
      _ExtentX        =   7223
      _ExtentY        =   661
      _Version        =   393216
      Appearance      =   1
      Scrolling       =   1
   End
   Begin VB.Frame Frame3 
      Caption         =   "Mensaje:"
      Height          =   2895
      Left            =   0
      TabIndex        =   4
      Top             =   1440
      Width           =   5415
      Begin VB.TextBox mensaje 
         Height          =   2535
         Left            =   120
         TabIndex        =   7
         Top             =   240
         Width           =   5175
      End
   End
   Begin VB.Frame Frame2 
      Caption         =   "Asunto:"
      Height          =   615
      Left            =   0
      TabIndex        =   2
      Top             =   720
      Width           =   5415
      Begin VB.TextBox asunto 
         Height          =   285
         Left            =   120
         TabIndex        =   3
         Top             =   240
         Width           =   5175
      End
   End
   Begin VB.Frame Frame1 
      Caption         =   "e-mail del destinatario:"
      Height          =   615
      Left            =   0
      TabIndex        =   0
      Top             =   0
      Width           =   5415
      Begin VB.TextBox email 
         Height          =   285
         Left            =   120
         TabIndex        =   1
         Top             =   240
         Width           =   5175
      End
   End
End
Attribute VB_Name = "Form3"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Private Sub Form_Load()
Me.Icon = Nothing
End Sub
