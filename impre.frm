VERSION 5.00
Begin VB.Form impre 
   Caption         =   "Form1"
   ClientHeight    =   11010
   ClientLeft      =   -930
   ClientTop       =   -330
   ClientWidth     =   15240
   LinkTopic       =   "Form1"
   ScaleHeight     =   11010
   ScaleWidth      =   15240
   WindowState     =   2  'Maximized
   Begin VB.VScrollBar VScroll1 
      Height          =   6135
      Left            =   0
      Max             =   15075
      TabIndex        =   1
      Top             =   0
      Width           =   255
   End
   Begin VB.PictureBox Picture1 
      AutoRedraw      =   -1  'True
      Height          =   11640
      Left            =   240
      ScaleHeight     =   11580
      ScaleWidth      =   15075
      TabIndex        =   0
      Top             =   -720
      Width           =   15135
   End
End
Attribute VB_Name = "impre"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Private Sub VScroll1_Change()
Picture1.Top = -1 * VScroll1.Value
End Sub
