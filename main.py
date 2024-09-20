"""
    Writtn by Juan Pablo Gutiérrez
    10 09 2024
"""
from datetime import datetime, timedelta

from algorithms.file_manager import getResponse, download, removeFile

from algorithms.code_receiver import getAllCodes

from algorithms.diary_filtering import checkForKeys

from algorithms.mail_sender import send_email

def main(date : str, to_email: list):
    codeList = getAllCodes(date=date)
    codeList = list(set(codeList))


    for code in codeList:
        email_body = f'El programa ha detectado actualizaciones en el DOF el día {date} con el siguientes código de diario:\n\n'

        response = getResponse(code)

        download(code, response)

        email_body += f'\nEste archivo está adjunto a este correo, pero se puede acceder a él en la siguiente dirección: https://sidofqa.segob.gob.mx/dof/sidof/documentos/pdf/{code}'

        send_email(subject="Actualización del DOF detectada", body=email_body, to_email=to_email, code=code)

if __name__ == '__main__':

    #main(date = (datetime.today()).strftime("%d-%m-%Y"),  to_email=["juguterr@gmail.com"])

    # Iterate over the last days
    for i in range(360): 
        print(f'Checking for updates on {(datetime.today() - timedelta(days=i)).strftime("%d-%m-%Y")}')

        main(date = (datetime.today() - timedelta(days=i)).strftime("%d-%m-%Y"),  to_email=["test@gmail.com"])
