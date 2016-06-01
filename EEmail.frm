VERSION 5.00
Object = "{248DD890-BB45-11CF-9ABC-0080C7E7B78D}#1.0#0"; "MSWINSCK.OCX"
Begin VB.Form EEmail 
   BorderStyle     =   1  'Fixed Single
   Caption         =   "Enviar por e-mail"
   ClientHeight    =   4830
   ClientLeft      =   45
   ClientTop       =   330
   ClientWidth     =   4695
   Icon            =   "EEmail.frx":0000
   LinkTopic       =   "Form1"
   MaxButton       =   0   'False
   MinButton       =   0   'False
   ScaleHeight     =   4830
   ScaleWidth      =   4695
   StartUpPosition =   2  'CenterScreen
   Begin VB.Frame Frame4 
      Caption         =   "Nombre del destinatario"
      Height          =   615
      Left            =   0
      TabIndex        =   11
      Top             =   1200
      Width           =   4695
      Begin VB.TextBox TxTnDeStInAtArIo 
         Height          =   285
         Left            =   120
         TabIndex        =   12
         Text            =   " "
         Top             =   240
         Width           =   4455
      End
   End
   Begin MSWinsockLib.Winsock Winsock1 
      Left            =   3240
      Top             =   120
      _ExtentX        =   741
      _ExtentY        =   741
      _Version        =   393216
   End
   Begin VB.CommandButton Command3 
      Cancel          =   -1  'True
      Caption         =   "Cancelar"
      Height          =   375
      Left            =   3480
      TabIndex        =   8
      Top             =   4440
      Width           =   1215
   End
   Begin VB.CommandButton Command2 
      Caption         =   "Enviar"
      Height          =   375
      Left            =   1440
      TabIndex        =   7
      Top             =   4440
      Width           =   1935
   End
   Begin VB.CommandButton Command1 
      Caption         =   "Vista preliminar"
      Height          =   375
      Left            =   0
      TabIndex        =   6
      Top             =   4440
      Width           =   1335
   End
   Begin VB.Frame Frame3 
      Caption         =   "Mensaje (se colocará antes que el presupuesto):"
      Height          =   1695
      Left            =   0
      TabIndex        =   4
      Top             =   2640
      Width           =   4695
      Begin VB.TextBox txtmensaje 
         Height          =   1335
         Left            =   120
         MultiLine       =   -1  'True
         ScrollBars      =   2  'Vertical
         TabIndex        =   5
         Top             =   240
         Width           =   4455
      End
   End
   Begin VB.Frame Frame2 
      Caption         =   "Asunto:"
      Height          =   615
      Left            =   0
      TabIndex        =   2
      Top             =   1920
      Width           =   4695
      Begin VB.TextBox txtasunto 
         Height          =   285
         Left            =   120
         TabIndex        =   3
         Top             =   240
         Width           =   4455
      End
   End
   Begin VB.Frame Frame1 
      Caption         =   "Destinatario:"
      Height          =   615
      Left            =   0
      TabIndex        =   0
      Top             =   480
      Width           =   4695
      Begin VB.TextBox txtdestinatario 
         Height          =   285
         Left            =   120
         TabIndex        =   1
         Top             =   240
         Width           =   4455
      End
   End
   Begin VB.Label lbloperacion 
      Caption         =   "nada"
      Height          =   255
      Left            =   960
      TabIndex        =   10
      Top             =   120
      Width           =   3735
   End
   Begin VB.Label Label1 
      Alignment       =   1  'Right Justify
      Caption         =   "Operación:"
      Height          =   255
      Left            =   0
      TabIndex        =   9
      Top             =   120
      Width           =   855
   End
End
Attribute VB_Name = "EEmail"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Option Explicit

Public LoginSucceeded As Boolean
Dim Response As String, Reply As Integer, DateNow As String
Dim first As String, Second As String, Third As String
Dim Fourth As String, Fifth As String, Sixth As String
Dim Seventh As String, Eighth As String, ninth As String
Dim Start As Single, Tmr As Single

Private Sub Command1_Click()
Select Case lbloperacion
Case "Donación"
Open "C:\windows\temp\Donacion.htm" For Binary As #1
'Put 1, , txtmensaje & vbNewLine & GenHTMLDonacion("Escribanía " & GetSetting("Presupuestos", "Escribania", "Nombre", "Ventura"), GetSetting("Presupuestos", "Escribania", "Direccion", "Corrientes 5 - 4º " & Chr(34) & "A" & Chr(34)), GetSetting("Presupuestos", "Escribania", "Telefonoemail", "Te: 4255715 - e-mail: gabventura@arnet.com.ar"), Donacion.partes, Donacion.VEconomico, Donacion.arAncel, Donacion.certificado, Donacion.aportes1, Donacion.aportes2, Donacion.anotacion, Donacion.goperativo, Donacion.total, Donacion.notros1, Donacion.otros1, Donacion.notros2, Donacion.otros2, Donacion.notros3, Donacion.otros3)
Close
Shell "C:\archivos de programa\Internet Explorer\iexplore.exe C:\windows\temp\Donacion.htm", vbMaximizedFocus
Case "Venta"
Open "C:\windows\temp\Venta.htm" For Binary As #1
'Put 1, , txtmensaje & vbNewLine & GenHTML("Escribanía " & GetSetting("Presupuestos", "Escribania", "Nombre", "Ventura"), GetSetting("Presupuestos", "Escribania", "Direccion", "Corrientes 5 - 4º " & Chr(34) & "A" & Chr(34)), GetSetting("Presupuestos", "Escribania", "Telefonoemail", "Te: 4255715 - e-mail: gabventura@arnet.com.ar"), Venta.partes, Venta.VEconomico, Venta.arAncel, Venta.certificado, Venta.aportes1, Venta.aportes2, Venta.reposicion, Venta.anotacion, Venta.goperativo, Venta.total, Venta.notros1, Venta.otros1, Venta.notros2, Venta.otros2, Venta.notros3, Venta.otros3)
Close
Shell "C:\archivos de programa\Internet Explorer\iexplore.exe C:\windows\temp\Venta.htm", vbMaximizedFocus
End Select
End Sub
Sub SendEmail(MailServerName As String, FromName As String, FromEmailAddress As String, ToName As String, ToEmailAddress As String, EmailSubject As String, EmailBodyOfMessage As String)
          
    Winsock1.LocalPort = 0 ' Must set local port to 0 (Zero) or you can only send 1 e-mail pre program start
    
If Winsock1.State = sckClosed Then ' Check to see if socet is closed
    DateNow = Format(Date, "Ddd") & ", " & Format(Date, "dd Mmm YYYY") & " " & Format(Time, "hh:mm:ss") & "" & " -0600"
    first = "mail from:" + Chr(32) + FromEmailAddress + vbCrLf ' Get who's sending E-Mail address
    Second = "rcpt to:" + Chr(32) + ToEmailAddress + vbCrLf ' Get who mail is going to
    Third = "Date:" + Chr(32) + DateNow + vbCrLf ' Date when being sent
    Fourth = "From:" + Chr(32) + FromName + vbCrLf ' Who's Sending
    Fifth = "To:" + Chr(32) + ToName + vbCrLf ' Who it going to
    Sixth = "Subject:" + Chr(32) + EmailSubject + vbCrLf ' Subject of E-Mail
    Seventh = EmailBodyOfMessage + vbCrLf ' E-mail message body
    ninth = "X-Mailer: EBT Reporter v 2.x" + vbCrLf ' What program sent the e-mail, customize this
    Eighth = Fourth + Third + ninth + Fifth + Sixth  ' Combine for proper SMTP sending

    Winsock1.Protocol = sckTCPProtocol ' Set protocol for sending
    Winsock1.RemoteHost = MailServerName ' Set the server address
    Winsock1.RemotePort = 25 ' Set the SMTP Port
    Winsock1.Connect ' Start connection
    
    WaitFor ("220")
    
    
    Winsock1.SendData ("HELO worldcomputers.com" + vbCrLf)

    WaitFor ("250")


    Winsock1.SendData (first)


    WaitFor ("250")

    Winsock1.SendData (Second)

    WaitFor ("250")

    Winsock1.SendData ("data" + vbCrLf)
    
    WaitFor ("354")


    Winsock1.SendData (Eighth + vbCrLf)
    Winsock1.SendData (Seventh + vbCrLf)
    Winsock1.SendData ("." + vbCrLf)

    WaitFor ("250")

    Winsock1.SendData ("quit" + vbCrLf)
    


    WaitFor ("221")
    MsgBox "E-mail enviado correctamente", vbInformation, "Envío por e-mail"
    Winsock1.Close
Else
    MsgBox (Str(Winsock1.State))
End If
   
End Sub

Sub WaitFor(ResponseCode As String)
    Start = Timer ' Time event so won't get stuck in loop
    While Len(Response) = 0
        Tmr = Start - Timer
        DoEvents ' Let System keep checking for incoming response **IMPORTANT**
        If Tmr > 50 Then ' Time in seconds to wait
            MsgBox "SMTP service error, timed out while waiting for response", 64
            Exit Sub
        End If
    Wend
    While Left(Response, 3) <> ResponseCode
        DoEvents
        If Tmr > 50 Then
            MsgBox "SMTP service error, impromper response code. Code should have been: " + ResponseCode + " Code recieved: " + Response, 64
            Exit Sub
        End If
    Wend
Response = "" ' Sent response code to blank **IMPORTANT**
End Sub

Private Sub Command2_Click()
MsgBox "Espere un momento hasta que aparesca" & vbNewLine & "un mensaje diciendo que el e-mail ha sido" & vbNewLine & " enviado", vbInformation, "Envío por e-mail"
Select Case lbloperacion
Case "Donación"
'SendEmail GetSetting("Presupuestos", "email", "Servidor", "smtp.arnet.com.ar"), GetSetting("Presupuestos", "email", "NRemitente", "Gabriel B. Ventura"), GetSetting("Presupuestos", "email", "email", "gabventura@arnet.com.ar"), TxTnDeStInAtArIo, txtdestinatario, txtasunto, txtmensaje & vbNewLine & GenHTMLDonacion("Escribanía " & GetSetting("Presupuestos", "Escribania", "Nombre", "Ventura"), GetSetting("Presupuestos", "Escribania", "Direccion", "Corrientes 5 - 4º " & Chr(34) & "A" & Chr(34)), GetSetting("Presupuestos", "Escribania", "Telefonoemail", "Te: 4255715 - e-mail: gabventura@arnet.com.ar"), Donacion.partes, Donacion.VEconomico, Donacion.arAncel, Donacion.certificado, Donacion.aportes1, Donacion.aportes2, Donacion.anotacion, Donacion.goperativo, Donacion.total, Donacion.notros1, Donacion.otros1, Donacion.notros2, Donacion.otros2, Donacion.notros3, Donacion.otros3)
Case "Venta"
'SendEmail GetSetting("Presupuestos", "email", "Servidor", "smtp.arnet.com.ar"), GetSetting("Presupuestos", "email", "NRemitente", "Gabriel B. Ventura"), GetSetting("Presupuestos", "email", "email", "gabventura@arnet.com.ar"), TxTnDeStInAtArIo, txtdestinatario, txtasunto, txtmensaje & vbNewLine & GenHTML("Escribanía " & GetSetting("Presupuestos", "Escribania", "Nombre", "Ventura"), GetSetting("Presupuestos", "Escribania", "Direccion", "Corrientes 5 - 4º " & Chr(34) & "A" & Chr(34)), GetSetting("Presupuestos", "Escribania", "Telefonoemail", "Te: 4255715 - e-mail: gabventura@arnet.com.ar"), Venta.partes, Venta.VEconomico, Venta.arAncel, Venta.certificado, Venta.aportes1, Venta.aportes2, Venta.reposicion, Venta.anotacion, Venta.goperativo, Venta.total, Venta.notros1, Venta.otros1, Venta.notros2, Venta.otros2, Venta.notros3, Venta.otros3)
End Select
End Sub

Private Sub Command3_Click()
Unload Me
End Sub

Private Sub Form_Load()
txtdestinatario = ""
txtasunto = ""
TxTnDeStInAtArIo = ""
txtmensaje = ""
End Sub

Private Sub lbloperacion_Change()
txtasunto = lbloperacion
End Sub

Private Sub Winsock1_DataArrival(ByVal bytesTotal As Long)

    Winsock1.GetData Response ' Check for incoming response *IMPORTANT*

End Sub
