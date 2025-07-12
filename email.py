import smtplib
from email.message import EmailMessage

def enviar_por_correo(archivo_bytes, destinatarios):
    msg = EmailMessage()
    msg['Subject'] = 'Informe generado'
    msg['From'] = 'tu_correo@gmail.com'
    msg['To'] = ', '.join(destinatarios)
    msg.set_content('Adjunto se encuentra el informe generado.')

    # Adjuntar archivo
    msg.add_attachment(archivo_bytes.getvalue(),
                       maintype='application',
                       subtype='vnd.openxmlformats-officedocument.wordprocessingml.document',
                       filename='informe.docx')

    # Enviar usando servidor SMTP (Gmail como ejemplo)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        import os
        smtp_pass = os.environ.get("GMAIL_PASS")
        smtp.login('adalig930@gmail.com', smtp_pass)
        smtp.send_message(msg)
