""" 
    Written by Juan Pablo Gutiérrez
    11 09 2024
"""
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

import os
from dotenv import load_dotenv

load_dotenv()

def send_email(subject : str, body : str, to_email :str, code : int):
    from_email = os.getenv("SENDER_EMAIL")
    password = os.getenv("SENDER_PASSWORD")

    # Create the email
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach the email body
    msg.attach(MIMEText(body, 'plain'))

    # Attach the PDF file
    with open(f'{code}.pdf', "rb") as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename= {code}.pdf')
        msg.attach(part)

    try:
        # Connect to the Gmail SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, password)
        
        # Send the email
        server.send_message(msg)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
    finally:
        server.quit()
